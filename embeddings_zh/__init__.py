#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2025 Chatopera Inc. <www.chatopera.com> All Rights Reserved
#
#
# File: /c/Users/Administrator/chatopera/embeddings-zh/embeddings_zh/__init__.py
# Author: Hai Liang Wang
# Date: 2025-05-30:10:07:37
#
#===============================================================================

"""
Embeddings Interfaces

https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings
"""
__copyright__ = "Copyright (c) Chatopera Inc. 2025. All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2025-05-30:10:07:37"

import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    raise RuntimeError("Must be using Python 3")
else:
    unicode = str

from typing import Any, Dict, List, Optional
import synonyms

class EmbeddingsZh():
    
    def __init__(self, **kwargs: Any):
        pass

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embeddings with Chatopera [Synonyms](https://github.com/chatopera/Synonyms) for chatbot, RAG.

        Args:
            texts: The list of texts to embed.

        Returns:
            List of embeddings, one for each text.
        """
        ret = []

        texts = list(map(lambda x: x.replace("\n", " "), texts))

        for text in texts:
            terms = synonyms.seg(text)[0]
            v = synonyms.sv(" ".join(terms))
            ret.append(v)

        return ret


    def embed_query(self, text: str) -> List[float]:
        """Compute query embeddings using Chatopera [Synonyms](https://github.com/chatopera/Synonyms) for chatbot, RAG.

        Args:
            text: The text to embed.

        Returns:
            Embeddings for the text.
        """
        return self.embed_documents([text])[0]



##########################################################################
# Testcases
##########################################################################
import unittest

# run testcase: python /c/Users/Administrator/chatopera/embeddings-zh/embeddings_zh/__init__.py Test.testExample
class Test(unittest.TestCase):
    '''
    
    '''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001(self):
        print("test_001")

def test():
    '''
    Run tests, two ways available
    '''

    # run as a suite
    #suite = unittest.TestSuite()
    #suite.addTest(Test("test_001"))
    #runner = unittest.TextTestRunner()
    #runner.run(suite)

    # run as main, accept pass testcase name with argvs
    unittest.main()

def main():
    test()

if __name__ == '__main__':
    main()
