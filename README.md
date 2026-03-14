# BioInform1 -- NGS Bioinformatics Pipeline

## Overview

BioInform1 is a simplified Next Generation Sequencing (NGS) pipeline
that processes genomic sequencing data from raw reads to aligned genomic
output.

## Pipeline Workflow

FASTQ → Quality Control → Alignment → SAM → BAM → Sorted BAM

## Tools Used

-   FastQC -- sequencing quality analysis
-   BWA -- DNA sequence alignment
-   Samtools -- genomic file processing

## Project Structure

BioInformatics/ │ └── BioInform1 ├── data ├── reference ├── scripts ├──
results ├── logs └── config

## Running the Pipeline

cd BioInformatics/BioInform1/scripts ./run_pipeline.sh

## Output Files

-   FastQC quality report (HTML)
-   SAM alignment file
-   BAM binary alignment file
-   Sorted BAM file

## Learning Goals

This project demonstrates:

-   Linux-based bioinformatics pipelines
-   NGS data processing
-   alignment algorithms
-   genomic data formats
-   reproducible data workflows
