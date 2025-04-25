# Código feito com o ChatGPT, a conversa pode ser vista em:
# https://chatgpt.com/share/680c0a11-5cb8-8005-bff3-654322d2790c

import pandas as pd
import subprocess
import os
import kagglehub

# Step 0: Download the dataset from Kaggle
path = kagglehub.dataset_download("dhruvildave/github-commit-messages-dataset")
file_path = os.path.join(path, 'full.csv')  # assuming the file is named full.csv

print("Path to dataset:", file_path)

target_repo = 'scikit-learn/scikit-learn'
chunk_size = 10000
repo_path = os.path.expanduser('~/repos/scikit-learn')

matching_chunks = []
chunk_count = 0

# Step 1: Read in chunks and filter
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    chunk_count += 1
    # Only print the chunk progress once
    print(f"Reading chunk {chunk_count}... Total rows: {len(chunk)}; Filtered rows: {len(chunk[chunk['repo'] == target_repo])}", end='\r', flush=True)

    # Filter the chunk for the specific repo
    filtered = chunk[chunk['repo'] == target_repo]

    # Only append non-empty chunks
    if not filtered.empty:
        matching_chunks.append(filtered)

print(f"\nFinished reading {chunk_count} chunks.")

# Combine filtered chunks into the final DataFrame
df = pd.concat(matching_chunks, ignore_index=True)

# Step 2: Get unique commit hashes
unique_commits = df['commit'].dropna().unique()

# Step 3: Extract only the diff section from git show
def extract_diff_only(full_output):
    lines = full_output.splitlines()
    for i, line in enumerate(lines):
        if line.startswith('diff --git'):
            return '\n'.join(lines[i:])
    return ''  # no diff found

# Step 4: Create mapping from commit hash to diff
commit_diff_dict = {}
commit_count = 0

for commit in unique_commits:
    commit_count += 1
    print(f"Processing commit {commit_count}/{len(unique_commits)}: {commit[:7]}...", end='\r', flush=True)

    try:
        result = subprocess.run(
            ['git', 'show', commit],
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8',
            errors='replace',
            check=True
        )
        commit_diff_dict[commit] = extract_diff_only(result.stdout)
    except subprocess.CalledProcessError as e:
        commit_diff_dict[commit] = f"Error: {e.stderr}"

print("\nFinished processing all commits.")

# Step 5: Map diffs to original dataframe
df['git_diff'] = df['commit'].map(commit_diff_dict)

# Step 6: Drop all rows with any NaN values
df = df.dropna()

# Step 7: Save final result as a Parquet file
output_path = 'scikit_learn_commits.parquet'
df.to_parquet(output_path, index=False)
print(f"Saved {len(df)} rows with git diffs to {output_path}.")
