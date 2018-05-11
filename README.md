This is the repository of examples for the book "Deep Learning Framework PyTorch: Introduction and Practice". But it can also serve as an independent introduction or tutorial for PyTorch.

## Content

The content of the book and this repository can be demonstrated by the following picture:
![Mind Map](http://7zh43r.com2.z0.glb.clouddn.com/del/mindmap.png)

This book is divided into two major parts:

**Fundamental Part** (the first 5 chapters) introduces the PyTorch, including the major components and some useful tools for deep learning. Jupyter Notebook is used for the code demonstration. Readers can modify the Jupyter notebooks to repeatedly try and run for better understanding.

- Chapter 2 introduces how to install and configure the PyTorch. It also provides a short introduction of PyTorch itself based on the official tutorial. Readers can take 1 or 2 hours for the introduction and choose which chapter to proceeded based on his or her interests.
- Chapter 3 introduces the multi-dimensional Tensor and dynamic graph autograd/Variable in PyTorch with examples. A linear regression example is implemented using both Tensor and autograd for user to compare the difference of the two. Design of the Tensor and the analysis of the autograd are also included in this chapter for user to master the two most important components of PyTorch.
- Chapter 4 introduces the neural network module nn in PyTorch. Layer, loss function and  optimizer are also introduced in this chapter. A less than 50 lines of code implementation of one time ImageNet champion ResNet is explained at the end of this chapter.
- Chapter 5 introduces the utility tools of data loader, GPU acceleration, serialization, and visualization.

**Practical Part** (chapter 6 to chapter 10) explains and implements several cool applications using PyTorch. This repository contains the complete code for the implementation together with the pre-trained models for user to play with.

- Chapter 6 is a transition chapter. It is not used for learning new functions or modules. Instead, a binary classification task of dog and cat, a classic competition from Kaggle, is implemented and explained step by step. It helps readers to review the knowledge of the previous 5 chapters. It also introduces some rules of organizing the code to make it more readable and maintainable. How to debug in PyTorch is also introduced in this chapter.
- Chapter 7 explores one of the hottest neural networks, the Generative Adversarial Networks (GAN). A anime character generator is implemented and explained with GAN. It can generate a variety of anime characters.
- Chapter 8 explains the of neural style. It walks you through the implementation of the neural algorithm of artistic style, which can turn your pictures into famous paintings.
- Chapter 9 introduces the basics of Natural Language Processing (NLP). It also explains the CharRNN. Then a project is developed for auto generation of Chinese Poem with model trained from tens of thousands of real Chinese poem from Tang Dynasty. The **style**, the **present moment** can be tuned. And It can even generate **acrostic poem**.
- Chapter 10 introduces image caption task. With the dataset from latest AI Challenger, it walks the reader through the implementation of a image caption project step by step.
- Chapter 11 (**new, experimental**) A voice recognition project form [Diamondfan](https://github.com/Diamondfan). Improvements are done in this project (including examples for image, text, and voice recognitions)


**Comments in the Notebook were from the early drafts, please forgive me for typos and lack of clarity**. I planned to remove all the comments in the notebook. But I chose not to for readers to understand the code better. I will review all the comments if I got time. But there is not commitment yet. 

## Have to buy the book?

The book is **not a must**. This repository has 50% text of the book and more than 90% of the code. For the first couple of chapters, almost the whole content is shown in the repository. You do not have to have the book to use this repository.

But, if you like to read a hard copy of the book, and not mind to spend a little amount of money to support my half year's work, a purchase of this book is appreciated.

## Instruction of the Code

- All code has been tested both in Python2 and in Python3
- The code in the practical part has been tested both on CPU and on GPU.
- ~~All the code are based on the PyTorch 0.2.0~~.  And I am committed to maintain the code at least to the version `0.4`

Currently, the code for the first 5 chapters has been updated to PyTorch 0.3.0. If you want to run it in PyTorch 0.2.0, please do
```
git checkout v0.2
```

You are welcome to open issues or send pull requests if you think there is any inappropriate or need-to-improve part.

## Configurations

1. Install[PyTorch](http://pytorch.org)，Please pick the versions that is on the official website, using anaconda, or pip. Please reference to the installation part for more options.

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
