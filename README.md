# medical-chatbot
 Building a general medical chatbot or focusing on a specific area like symptom checking, disease diagnosis, mental health support, or medical recommendations


# medical-chatbot

### Table of Contents
- [Demo](#demo)
- [Overview](#overview)
- [Motivation](#motivation)
- [Technical Aspect](#technical-aspect)
- [Installation](#installation)
- [Run](#run)
- [Deployment on Render](#deployment-on-render)
- [Directory Tree](#directory-tree)
- [To Do](#to-do)
- [Bug / Feature Request](#bug--feature-request)
- [Technologies Used](#technologies-used)
- [Team](#team)
- [License](#license)
- [Credits](#credits)

---
## Demo
This project classifies poems into different categories using machine learning.<br>
**Link to Demo:** [medical-chatbot](#) 





![Poem-Classification](https://i.imgur.com/X3MkbX1.jpeg)

---

## Overview
The Poem Classification project utilizes Natural Language Processing (NLP) and machine learning to categorize poems. This model is capable of understanding different poetry styles, such as Haiku, Sonnet, Free Verse, and more. It is designed to help literature enthusiasts, educators, and researchers analyze poetry more effectively.

Key Features:

- Preprocessing of Poem Text Data

- Classification using Advanced ML and NLP Models

- Interactive Web Application for Real-time Predictions

- Deployment on Render for Public Access
---

## Motivation

Poetry is a unique form of text that expresses emotions, and classifying it into different genres helps in literary analysis,
recommendation systems, and educational tools. This project showcases the power of deep learning in text classification.
---

## Technical Aspect
### Training Recommendation Model:

Data Collection:

- A dataset of poems is sourced from public repositories and literature archives.

Preprocessing:

- Text cleaning (removal of special characters, punctuation, and stopwords).

- Tokenization and lemmatization.

- Vectorization using TF-IDF or Word Embeddings (Word2Vec, GloVe).

Model Training:

- Classifiers Used: Naive Bayes, Support Vector Machine (SVM), and BERT.

- Hyperparameter tuning for improved performance.

Model Evaluation:

- Metrics: Accuracy, Precision, Recall, and F1 Score.

Web App Development:

- Built using Flask.

- User input for poem text classification.

- Deployed on Render.
---

## Installation
The Code is written in Python 3.10. Install the required packages and libraries by running:

```bash
pip install -r requirements.txt
```

## Run
To run the Flask web app locally:

```bash
python app.py
```

## Deployment on Render

To deploy the Flask web app on Render:
- Push your code to GitHub.
- Log in to Render and create a new web service.
- Connect the GitHub repository.
- Configure environment variables (if any).
- Deploy and access your app live.

## Directory Tree 
```
📂 project-root/
│── 📂 data/
│── 📂 model/
│── 📂 notebook/
│── 📂 static/
│── 📂 templates/
│── 📂 venv/   
│── 📄 .gitignore
│── 📄 app.py
│── 📄 LICENSE
│── 📄 README.md
│── 📄 requirements.txt
│── 📄 template.py
```

## To Do

- Expand dataset for better generalization.

- Implement deep learning models like BERT or GPT.

- Enhance the web app with visualization features.

- Optimize model inference speed.

## Bug / Feature Request
If you encounter any bugs or want to request a new feature, please open an issue on GitHub. Contributions are welcome!

## Technologies Used
- Python 3.10
- scikit-learn
- Flask (for web app development)
- Render (for hosting and deployment)
- pandas (for data manipulation)
- numpy (for numerical computations)

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/260px-Scikit_learn_logo_small.svg.png" width=170>](https://pandas.pydata.org/docs/)
[<img target="_blank" src="https://miro.medium.com/v2/resize:fit:720/format:webp/0*RWkQ0Fziw792xa0S" width=170>](https://pandas.pydata.org/docs/)
[<img target="_blank" src="https://icon2.cleanpng.com/20180829/okc/kisspng-flask-python-web-framework-representational-state-flask-stickker-1713946755581.webp" width=170>](https://flask.palletsprojects.com/en/stable/) 
[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/512px-NumPy_logo_2020.svg.png" width=200>](https://numpy.org/doc/) 
---

## Team
This project was developed by:
[![Bablu kumar pandey](https://github.com/Creator-Turbo/images-/blob/main/resized_image.png?raw=true)](ressume_link) |
-|

**Bablu Kumar Pandey**

- [GitHub](https://github.com/Creator-Turbo)  
- [LinkedIn](https://www.linkedin.com/in/bablu-kumar-pandey-313764286/)
- **Personal Website**: [My Portfolio](https://creator-turbo.github.io/Creator-Turbo-Portfolio-website/)

## License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this software under the terms of the MIT License. For more details, see the [LICENSE](LICENSE) file included in this repository.

## Credits

Special thanks to the contributors of the scikit-learn library for their fantastic machine learning tools.