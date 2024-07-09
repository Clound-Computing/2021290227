# 2021290227
这是一篇来自ACL2021的文章，原文链接如下：

[Multimodal Fusion with Co-Attention Networks for Fake news Detection](https://aclanthology.org/2021.findings-acl.226.pdf)

官方代码地址： [GitHub-wuyang45/MCAN_code](https://github.com/wuyang45/MCAN_code)

本项目是对原文MCAN思路的复现，但使用了[GossipCop数据集](https://github.com/junyachen/Data-examples#integration-based-legitimate)，旨在对原文MCAN模型进行测试并验证其在更广泛的数据集上的适用性。

## Main idea
社交媒体上多模态假新闻检测的独特挑战之一是如何融合多模态特征。人们在阅读图像新闻时，往往先观察图像，然后再阅读文字。这个过程可能会重复多次，不断融合图像和文本信息。受此启发，MCAN旨在学习所有模式之间的相互依赖性，以有效地融合它们，从而提高假新闻检测的性能

## Architecture
首先，我们提取图像的语义级和物理级特征以及文本特征。然后我们使用深度共同注意网络将它们融合在一起，该网络由多个共同注意层组成。最后利用多模态融合表示来判断输入新闻的真实性

## Create the env
首先创建代码所需的环境，推荐使用anaconda创建虚拟环境。代码运行所需要的关键包已在requirements.txt中列出。

The python version is python-3.8.16. The detailed version of some packages is available in requirements.txt. You can install all the required packages using the following command:
```
conda install --yes --file requirements.txt
```

## Data
数据集可以从[GossipCop数据集](https://github.com/junyachen/Data-examples#integration-based-legitimate)中获取，本模型同时我们使用了图片信息以及文本信息，将下载后的json文件重新命名，以满足后面数据预处理的读取。命名规则为`gossipcop_v3-X.json`，X为1~6。
