#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import FileInfo
def listDirectory(directory, fileExtList):
    u"zwraca liste obiektów zawierajacych metadane dla plików o podanych rozszerzeniach"
    fileList = [os.path.normcase(f) for f in os.listdir(directory)]
    fileList = [os.path.join(directory, f) for f in fileList
                if os.path.splitext(f)[1] in fileExtList]

    