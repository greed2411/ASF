# Anti Spam Filter

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/greed2411/ASF/commits/master)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/greed2411)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub issues](https://img.shields.io/github/issues/greed2411/ASF.svg)](https://github.com/greed2411/ASF/issues)
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/greed2411/badges)

## What is ASF?

A Spam Filter built for Pugaar.

## What is Pugaar?

*Pugaar*, is an Android and Web application dedicated for lodging complaints and pettty issues related to the maintenance of [VIT University, Vellore Men's Hostel](https://en.wikipedia.org/wiki/Vellore_Institute_of_Technology).
Our goal is to eradicate all the handwritten complaints which takes days to process, by automating the whole process. Once a complaint is into the system, an employee is directly informed using SMS regarding the issue and the details of the one who made the complaint.

## Presenting Team members:

Android Application by:
 * [@MINOSai](https://github.com/MINOSai) 

Web Application by : 
 * [@MINOSai](https://github.com/MINOSai): made it with [Vue.js](https://vuejs.org/)
 * [@bhaveshpraveen](https://github.com/bhaveshpraveen):  made the REST API using [Django](https://www.djangoproject.com/).
 * [@greed2411](https://github.com/greed2411):  made the Spam filter with custom dataset and [scikit-learn](http://scikit-learn.org/stable/).
 
## What does ASF do?

ASF by heart removes spam, i.e., selectively passes complaints dedicated for VIT University Men's Hostel.
It passes complaints which fall under the category of Electrical, Toiletries, Room and Air Conditioners.
Examples include `door knob broken`, `smoke alarm is not working`, `bathroom tap is loose`, `AC not cool enough`

## What about the Dataset and the algorithm?

Dataset was handtyped out of the past few years records of complaints under [J block](https://www.quora.com/How-is-the-J-block-of-VIT-Vellore).

As of the algorithm, MultinomialNB is being used here.

### Technical stuff :

## Why `Naive Bayes`?

Naive Bayes, the most core feature of it is the independence. [Bayes thoerem](https://brilliant.org/wiki/bayes-theorem/) is based on independence of the events, that means here presence of one word shouldn't affect the presence of another word. This is advantageous and disadvantageous(the reason it's being called Naive) based on how people manipulate their words. For a basic hostel complaint, a ML algorithm such as NB is enough. We could have gone with DenseNets if we had more data. But it's a shame we only had 1500 records.

## About the model:

### Classification accuracy:

Testing accuracy of Naive Bayes model is `99.436 %` on 25% of the actual data. This shows how good is the feature engineering and  how good the model is at generalzing.

### Confusion matrix:

|**Model**                    |**Spam**|**Complaint**|
|-----------------------------|------------|------------|
|**Spam** | 190 |0|
|**Complaint**|2|163|

 * Spam and Spam intersection talks about the `True Negatives` - 190,
 * Spam and Complaint intersection talks about the `False Positives` - 0, (The spam which got classfied as complaint)
 * Complaint and Spam intersection talks about the `False negatives` - 2, (The complaints which got classified as spam)
 * Complaint and Complaint intersection talks about the `True Positives` - 163.

### For prototyping

The model was dumped into a [pickle](https://docs.python.org/3/library/pickle.html) file using [joblib](https://pypi.python.org/pypi/joblib) to [spam_data_pugaar.pkl](https://github.com/greed2411/ASF/blob/master/spam_data_pugaar.pkl) and [Pipeline](http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) class.

## Necessary libraries :

* [pandas](https://pandas.pydata.org/pandas-docs/stable/) - For reading the data and manipulation.
* [scikit-learn](http://scikit-learn.org/stable/) - For preprocessing, feature engineering and run [MultinomialNB](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)
* [joblib](https://pypi.python.org/pypi/joblib) - For reading and storing the model as numpy records, much faster than ordinary pickling.

## You can try it by:

Get the repository on your local machine,

```
git clone https://github.com/greed2411/ASF.git
```

## Examples and Usage :

If the model sees the statement as a `complaint` it returns `True` else, if it is a `spam` it returns `False`.

```python3
>>> from asf import check
>>> check('tubelight broken.')
True        # satisfies as a complaint
>>> check('floor mopping')
True
>>> check('send me nudes xD')
False       # doesn't satisfy as a complaint
>>> check('Bahen ke laude')
False
>>> check("रंडी")
False
>>> check(None)
True
```

## Tested and developed on :

  **Ubuntu 16.10 , Python 3.6.0 |Anaconda 4.3.1 (64-bit) and scikit-learn version : 0.18.1**
