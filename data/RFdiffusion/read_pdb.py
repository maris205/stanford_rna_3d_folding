# -*- coding: utf-8 -*-
# @Time    : 2025/3/9  23:47
# @Author  : mariswang@rflysim
# @File    : read_pdb.py
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-
import os
import pandas as pd

#download data from https://www.kaggle.com/datasets/andrewfavor/uw-synthetic-rna-structures
# then unzip and set the path to the input_dir

def parse_pdb_line(line):
    """解析单行 PDB 数据（同上，略作简化）"""
    record_type = line[0:6].strip()
    if record_type not in ["ATOM", "HETATM"]:
        return None
    return {
        "atom_name": line[12:16].strip(),
        "residue_name": line[17:20].strip(),
        "chain": line[21],
        "residue_id": int(line[22:26].strip()),
        "x": float(line[30:38].strip()),
        "y": float(line[38:46].strip()),
        "z": float(line[46:54].strip()),
    }


def process_pdb_file(file_path):
    """处理单个 PDB 文件（同上）"""
    data = []
    with open(file_path, "r") as f:
        for line in f:
            parsed = parse_pdb_line(line.strip())
            if parsed:
                data.append(parsed)
    df = pd.DataFrame(data)
    c1_df = (
        df[df["atom_name"] == "C1'"]
        .sort_values(["chain", "residue_id"])
        .drop_duplicates(subset=["chain", "residue_id"])
        .assign(resid=lambda x: range(1, len(x) + 1))
        [["residue_name", "resid", "x", "y", "z"]]
    )
    filename = os.path.basename(file_path)
    c1_df.insert(0, "ID", filename)
    c1_df.columns = ["ID", "resname", "resid", "x_1", "y_1", "z_1"]
    return c1_df


def batch_pdb_to_csv(input_dir, output_csv):
    """递归遍历所有子目录，处理 PDB 文件"""
    all_dfs = []
    # 递归遍历目录树
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.lower().endswith(".pdb"):
                file_path = os.path.join(root, filename)
                try:
                    df = process_pdb_file(file_path)
                    all_dfs.append(df)
                    print(f"Processed: {file_path} (residues: {len(df)})")
                except Exception as e:
                    print(f"Error in {file_path}: {str(e)}")

    if all_dfs:
        final_df = pd.concat(all_dfs, ignore_index=True)
        final_df.to_csv(output_csv, index=False)
        print(f"合并完成: 共 {len(final_df)} 个残基，保存到 {output_csv}")
    else:
        print("未找到任何 PDB 文件")


# 使用示例
batch_pdb_to_csv(
    input_dir="archive\compile_all",  # 主目录（包含子目录）
    output_csv="rna_all_c1_coordinates.csv"
)