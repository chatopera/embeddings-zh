#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===============================================================================
#
# Copyright (c) 2025 Hai Liang Wang<hailiang.hl.wang@gmail.com> All Rights Reserved
#
#
# File: /c/Users/Administrator/chatopera/embeddings-zh/test.py
# Author: Hai Liang Wang
# Date: 2025-08-22:18:08:23
#
# ===============================================================================

"""
This script does not support python2.
"""
__copyright__ = "Copyright (c) 2025 Hai Liang Wang<hailiang.hl.wang@gmail.com> All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2025-08-22:18:08:23"

import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, curdir)

from embeddings_zh import EmbeddingsZh

emb = EmbeddingsZh()

print("Embed query")
print(emb.embed_query("你是冬天里的一把火"))

print("Embed doc")
print(emb.embed_documents(["你是冬天里的一把火", "你是冬天里的一把火"]))