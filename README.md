# Neural-Artistic-Style-Video-
Implementation of Neural Style Transfer on Video.

![](https://github.com/feziodoshi/Neural-Artistic-Style-Video-/blob/master/video/neural_style_1.gif)

Contributers : [Fenil Doshi](https://github.com/feziodoshi), [Rohan Pooniwala](https://github.com/rohanpooniwala), [Rohit Saha](https://github.com/RohitSaha), [Raghav Gupta](https://github.com/raghavgupta0296)

# Neural Artistic Style Implementation

We mainly used the following research papers to implement Neural Artistic Style

<ul>
<li> Implementation of Neural Style Transfer from the paper <a href="http://arxiv.org/abs/1508.06576">A Neural Algorithm of Artistic Style</a> in Keras 1.2.0

<li> Color Preservation is based on the paper [Preserving Color in Neural Artistic Style Transfer](https://arxiv.org/abs/1606.05897).

<li> Masked Style Transfer is based on the paper [Show, Divide and Neural: Weighted Style Transfer](http://cs231n.stanford.edu/reports2016/208_Report.pdf)
</ul>

And also took help from the repository [Neural-Style-Transfer](https://github.com/titu1994/Neural-Style-Transfer/) 

# Compatibility

We are using Keras 1.2.1 with Tensorflow backend Using CUDA on Windows 10. But it should work in Linux with/without CUDA using same keras version.

# Speed
On a 1070 Laptop GPU, the time required for each epoch depends on mainly image size (gram matrix size) :

<ul>
<li>For a 400x400 gram matrix, each epoch takes approximately 7-9 seconds. 
<li>For a 512x512 gram matrix, each epoch takes approximately 15-16 seconds. 
<li>For a 600x600 gram matrix, each epoch takes approximately 23-25 seconds. 
</ul>
