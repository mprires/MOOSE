#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------------------------------------------------
# Author: Lalith Kumar Shiyam Sundar
# Institution: Medical University of Vienna
# Research Group: Quantitative Imaging and Medical Physics (QIMP) Team
# Date: 13.02.2023
# Version: 2.0.0
#
# Description:
# This module contains the urls and filenames of the models and binaries that are required for the moosez.
#
# Usage:
# The variables in this module can be imported and used in other modules within the moosez to download the necessary
# binaries and models for the moosez.
#
# ----------------------------------------------------------------------------------------------------------------------

MODELS = {
    "clin_ct_bones": {
        "url": "https://example.com/lungs_model.zip",
        "filename": "clin_ct_bones_model.zip",
        "directory": "clin_ct_bones_model",
    },
    "clin_ct_ribs": {
        "url": "https://example.com/bones_model.zip",
        "filename": "clin_ct_ribs_model.zip",
        "directory": "clin_ct_ribs_model",
    },
    "clin_ct_vertebrae": {
        "url": "https://example.com/vertebrae_model.zip",
        "filename": "clin_ct_vertebrae_model.zip",
        "directory": "clin_ct_vertebrae_model",
    },
    "clin_ct_muscles": {
        "url": "https://example.com/muscles_model.zip",
        "filename": "clin_ct_muscles_model.zip",
        "directory": "clin_ct_muscles_model",
    },
    "clin_ct_lungs": {
        "url": "https://example.com/ribs_model.zip",
        "filename": "clin_ct_lungs_model.zip",
        "directory": "clin_ct_lungs_model",
    },
    "clin_ct_fat": {
        "url": "https://example.com/fat_model.zip",
        "filename": "clin_ct_fat_model.zip",
        "directory": "clin_ct_fat_model",
    },
    "clin_ct_vessels": {
        "url": "https://example.com/vessels_model.zip",
        "filename": "clin_ct_vessels_model.zip",
        "directory": "clin_ct_vessels_model",
    },
    "clin_ct_organs": {
        "url": "https://example.com/organs_model.zip",
        "filename": "clin_ct_organs_model.zip",
        "directory": "clin_ct_organs_model",
    },
    "clin_pt_fdg_tumor": {
        "url": "https://example.com/fdg_tumor_model.zip",
        "filename": "clin_pt_fdg_tumor_model.zip",
        "directory": "clin_pt_fdg_tumor_model",
    },
    "clin_ct_all": {
        "url": "https://example.com/ct_all_model.zip",
        "filename": "clin_ct_all_model.zip",
        "directory": "clin_ct_all_model",
    },
    "clin_fdg_pt_ct_all": {
        "url": "https://example.com/fdg_pt_ct_all_model.zip",
        "filename": "clin_fdg_pt_ct_all_model.zip",
        "directory": "clin_fdg_pt_ct_all_model",
    },
    "preclin_mr_all": {
        "url": "https://example.com/mr_all_model.zip",
        "filename": "preclin_mr_all_model.zip",
        "directory": "preclin_mr_all_model",
    },

}
