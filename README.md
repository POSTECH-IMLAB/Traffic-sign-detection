# Traffic-sign-detection

Created by Junghyun Hong and Daijin Kim at POSTECH IM LAB


## Overview

Detect and recognize traffic signs based on CNN.

This is based on Tsinghua Tencent 100k network (https://github.com/asyncbridge/tsinghua-tencent-100k).

We modified the network for korean traffic signs.

Becasue korean traffic sign datasets usually does not contain ground-truth for mask, we do not use pixel data.

Network is only composed of detection branch and classification branch.


## How to download materials

You can download trained weight file from following link.

Mean file (https://drive.google.com/open?id=1CKp6UAAwGQoDHghs-URS2t6DcVBAr9Zm)

Trained weight file 
 - trained.caffemodel (https://drive.google.com/open?id=1o54zOxlQbfD_-JLYmOWTS8k_NxFxUfvh)
 - trained.solverstate (https://drive.google.com/open?id=12D-MObATjNXT18OcRk8QQANsV82yWuBH)
 

## How to run

Install caffe and pycaffe first.

Or use the pre-built library that is uploaded in this repository (python folder).

Refer demo.py how to run this program.

