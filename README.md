# Technical Challenge
## SARAO Data Science Technical Challenge


_In this technical challenge we want to test for basic skills such as python coding, ability to handle data and reuse open-source code etc., but also to explore more intangible skills such as flexibility, creativity, independence, communication, ability to relearn and teach yourself, ability to implement ideas, ability to solve challenging problems and to scale them to handle large volumes of data._


##QUESTIONS

### Exact image repetition

_For the first question your goal is to write a python function to determine whether a test image is identical to any image in the Training directory of images. In addition to working code please outline your algorithm and briefly discuss its potential limitations and how you might speed it up._

 A naive solution to this problem is to directly compare the byte values of each image file in the Testing directory to the target image, and print the boolean response to the command line. One could also convert the image files to an array (numpy) in memory. When invoked with arguments pointing to the test image and database directory respectively, the python script compareTwoImagesExact.py will return if any of the database images is an exact binary match to the test image, and also if the numpy representations of the two images exactly match.

Of course there are serious limitations to this approach:
    
* for the binary comparison to succeed, the files must be precisely the same; one is unable to determine similarity of images if they are of different file formats, even the same class of file format, even if the images are otherwise identical in all respects.
* the numpy representation (`bit map' comparison) is marginally better, but not by much.
* any image modification, such as rotations, translations, blurring, the addition of noise, scaling, cropping will result in failure of comparison.
* this method is not optimised for speed in any way.

###Image repetition with resizing

_We next want to check if a new test image is the same as any of the training data, but this time allowing for possible resizing of the test image (you may assume the aspect ratio of the two images is the same if they have been resized). Write a python function to solve this problem and briefly describe your solution._

###Image repetition with blurring or added noise

A friend of yours decides to try to fool your system by messing with the test images before you receive them. She does this by Gaussian blurring some of the images or by adding a small amount of noise to each pixel in the image. Design a simple machine learning algorithm that can handle such types of image distortions of the images, as well the cases already discussed in questions 1 and 2.
Suppose you want a False Positive to False Negative rate of 2-1 (i.e., for every image that you incorrectly exclude from your database, you are willing to accept two images that should have been excluded because they are replicas of images in your database). How would you go about achieving that ratio, assuming you had a sufficiently large training set of images?
Write python code to solve this for an arbitrary input test image. Discuss your solution in detail and why you chose it. Also discuss other potential approaches to the problem and their pros and cons.

4. Adding Metadata
You notice that each training image in your database, and every new test image, also comes with a metadata tag telling you where it came from.
Let’s call this tag X. After some calculation you find that certain tags are more likely to correspond to images already in your dataset than others. Using appropriate pseudo-code or equivalently clear writing that would allow someone to begin coding your algorithm, describe how you would systematically use this metadata information to reduce your false positive and false negative error rate in discarding images?

5. Scaling to Large Datasets
How would the algorithms and ideas you presented in questions 3 and 4 scale to a large number of test and training images with unknown noise/blurring in each image? Please comment on the computational efficiency of your algorithms? What could be done to possibly make them more efficient? (Imagine you were doing this for the Google Image database!)

Closing Question
• Do you think this set of challenges missed some important data science skills that you have? If so please let us know. This is a chance to let us know what your super skills are!
