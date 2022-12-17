# EMAIL - SMS SPAM🚫 CLASSIFIER
![Display Image](https://github.com/amanastro7/email-sms-spam-classifier/blob/main/spam.jpg)



## WEB APP 🖥️
You Can Check The Deployed App On [Streamlit](https://amanastro7-email-sms-spam-classifier-sms-email-p7jnwf.streamlit.app/).

Here's a screenshot of the same:

![STREAMLIT SCREENSHOT](https://github.com/amanastro7/email-sms-spam-classifier/blob/main/images/streamlit_img.png)

Also Deployed On [HuggingFace Space](https://huggingface.co/spaces/amanastro07/sms-email-spam-clsfr)
(but it loads painfully slow as it is running on CPU).

Here's a screenshot of the same:

![HUGGING FACE SPACE SCREENSHOT](https://github.com/amanastro7/email-sms-spam-classifier/blob/main/images/image.png)



## SUMMARY 📝
An EMAIL SMS SPAM CLASSIFIER is a machine learning web application that is designed to identify and classify spam messages in email and SMS (short message service) communication channels. The web application uses machine learning algorithms to analyze the content and features of incoming messages and determine whether they are likely to be spam or legitimate. This can help to protect users from phishing scams, fraudulent offers, and other forms of spam that can be harmful or annoying. The machine learning model is trained on a dataset of labeled spam and non-spam messages, and it can be updated and improved over time as new spam messages are encountered.



## DATASET 📁
The dataset used for this project was found on [Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset). The SMS Spam Collection is a set of SMS tagged messages that have been collected for SMS Spam research. It contains one set of SMS messages in English of 5,574 messages, tagged ham (legitimate) or spam.



## MACHINE LEARNING MODEL USED ⚙️🛠️
**Naive Bayes** is a machine learning algorithm that is used for classification tasks. It is based on the **Bayes Theorem** which states that the probability of an event occurring is equal to the prior probability of the event multiplied by the likelihood of the event given some evidence. In the case of **Multinomial Naive Bayes**, the evidence is the frequency of words in a document, and the event is the class to which the document belongs.

The **Multinomial Naive Bayes** algorithm works by calculating the probability that a document belongs to a particular class, given the frequency of words in the document. It does this by assuming that each word in the document is independent of the others, and that the probability of each word occurring is determined by its frequency in the overall training set.
![BayesTh](https://user-images.githubusercontent.com/56089248/208252941-57e68b83-a1b7-4232-8e41-d5999456ccb7.png)



## MODEL SCORES 📊📉
The Dataset was trained on various classification algorithms like **LogisticRegression, SVC, GaussianNB, MultinomialNB, BernoulliNB, DecisionTreeClassifier, KNeighborsClassifier, RandomForestClassifier, AdaBoostClassifier, BaggingClassifier, ExtraTreesClassifier, GradientBoostingClassifier and XGBClassifier**.

The MULTINOMIAL BNAIVE BAYES gave us a better metrics >>> **ACCURACY** of the model was 97% and **PRECISION** was 1. Since we had an unbalanced dataset, so **Multinomial NB** was choosen as it had a precision of 1.



## VIDEO DEMO OF THE WEB APP 📱
Press ▶️ button to watch the video.

