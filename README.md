This the code repository for the book "Deep Learning Framework PyTorch: Introduction and Application". But it can also serves as an independent introduction or tutorial for PyTorch.

## Content

The content of the book and code hub can be demonstrated by the following picture:
![Mind Map](http://7zh43r.com2.z0.glb.clouddn.com/del/mindmap.png)

This book is divided into two major parts:

**Fundamental Part** (the first 5 chapters) introduces the PyTorch, includeing the major components and some useful tools for deep learning. Jupter Notebook is used for the code demonstration. Readers can modify the Jupyter notebooks to repeatedly try and run for better understanding.

- Chapter 2 introduces how to install and configure the PyTorch. It also provides a short introduction of PyTorch itself based on the officail tutorial. Readers can take 1 or 2 hours for the introduction and choose which chapter to proceeded based on his or her interests.
- Chapter 3 introduces the multi-dimentional Tensor and dynamic graph autograd/Variable in PyTorch with examples. A linear regression example is implemented using both Tensor and autograd for user to compare the difference of the two. Design of the Tensor and the a analysis of the autograd are also included in this chapter for user to master the two most important components of PyTorch.
- Chapter 4 introduces the nural network module nn in Pytorch. Layer, loss function and  optimzer are also introduced in this chapter. A less than 50 lines of code implmentation of one time ImageNet champion Resnet is explained at the end of this chapter.
- Chapter 5 introduces the utility tools of data loader, GPU acceleration, serialization, and visualization.

**Practical Part** (chapter 6 to chapter 10) eplains and implements several cool applications using PyTorch. This repository contains the complete code for the implementation together with the pre-trained models for user to play with.

- Chapter 6 is a transition chapter. It is not used for learning new functions or modules. Instead, a binary classification task of dog and cat, a classic competition from Kaggle, is implemented and explained step by step. It helps readers to review the knowlege of the previous 5 chapters. It also introduces some rules of organizing the code to make it more readable and maintainable. How to debug in PyTorch is also introduced in this chapter.
- 第七章为读者讲解了当前最火爆的生成对抗网络（GAN），带领读者从头实现一个动漫头像生成器，能够利用GAN生成风格多变的动漫头像。
- Chapter 7 explores one of the hostest nuraul networks, the Generative Adversarial Networks (GAN). A anime character generator is implemented and explained with GAN. TODO
- 第八章为读者讲解了风格迁移的相关知识，并带领读者实现风格迁移网络，将自己的照片变成高大上的名画。
- Chapter 8 eplains the knowlege of neural style. TODO
- Chapter 9 introduces the basics of Natural Language Processing (NLP). It also explains the CharRNN. Then a program is developed for auto generation of Chinese Poem with model trained from tens of thousands of real Chinese poem from Tang Dynasty. The **style**, the **present moment** can be tuned. And It can even generate **acrostic poem**.
- Chapter 10 introduces image caption task. With the dataset from latest AI Challenger, it walks the reader throgh the implementation of a image caption project step by step.
- Chapter 11 (**new, experimental**) A voice recognition project form [Diamondfan](https://github.com/Diamondfan). Improvents are done in this project (including examples for image, text, and voice recognitions)


**Comments in the Notebook were from the early drafts, please forgive me for typos and lack of clarity**. I planned to remove all the comments in the notebook. But I chose not to for readers to understand the code better. I will review all the comments if I got time. But there is not commitment yet. 

## Have to buy the book?

The book is **not a must**. This repository has 50% text of the book and more than 90% of the code. For the first couple of chapters, almost the whole content is shown in the repository. You do not have to have the book to use this repository.

But, if you like to read a hard copy of the book, and not mind to spend a little amount of money to support my half year's work, a purchase of this book is appreciated.

## Instruction of the Code

- All code has been tested both in Python2 and in Python3
- The code in the practical part has been tested both on CPU and on GPU.
- ~~All the code are based on the PyTorch 0.2.0~~.  And I am committed to mained the code at least to the version `0.4`

Currently, the code for the first 5 chapters has been updated to PyTorch 0.3.0. If you want to run it in PyToch 0.2.0, please do
```
git checkout v0.2
```

You are welcome to open issues or send pull requests if you think there is any inappropriate or need-to-improve part.

## Configurations

1. Install[PyTorch](http://pytorch.org)，Please pick the verions that is on the official website, using anaconda, or pip. Please refere to the installation part for more opitons.

2. Clone this repository

   ```python
   git clone https://github.com/chenyuntc/PyTorch-book.git
   ```

3. Install dependencies

   ```python
   cd pytorch-book && pip install -r requirements.txt
   ```

## Visdom load failure and its solution
**The latest version of the visdom has solved this problem. Please upgrade it."
```
pip install --upgrade visdom
```
The previous [solution](https://github.com/chenyuntc/pytorch-book/blob/2c8366137b691aaa8fbeeea478cc1611c09e15f5/README.md#visdom%E6%89%93%E4%B8%8D%E5%BC%80%E5%8F%8A%E5%85%B6%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88) is no long necessaray. And it has been deleted.

## ^_^

Please help to open issues for bugs or clarity of any part of content.


Pull requests are welcome.

Happy Coding!

![](http://img14.360buyimg.com/n1/jfs/t13339/32/2463730198/217483/e8148c6b/5a41277dNbd1470c1.jpg)

- [purchase from jd.com](https://search.jd.com/Search?keyword=pytorch%20入门与实践&enc=utf-8&wq=pytorch%20入门与实践&pvid=8b0d91d7108845ad8cbaf596326f3eb3)
- [purchase from dangdang.com](http://search.dangdang.com/?key=pytorch%20%C8%EB%C3%C5%D3%EB%CA%B5%BC%F9&act=input)
