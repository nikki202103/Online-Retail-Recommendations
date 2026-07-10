# 🛍️ Online Retail Recommendation System

## 📌 Project Overview

The **Online Retail Recommendation System** is a Python-based project that recommends products similar to the one selected by the user. It uses **Cosine Similarity** from Scikit-learn to compare products based on their features and suggest relevant recommendations.

This project demonstrates the basic concept of recommendation systems and is suitable for beginners learning Machine Learning and Python.

---

## 🚀 Features

* Recommend similar products
* Simple and beginner-friendly implementation
* Uses Cosine Similarity for recommendations
* Built with Python and Scikit-learn
* Easy to modify with your own dataset

---

## 🛠️ Technologies Used

* Python 3
* Pandas
* Scikit-learn

---

## 📂 Project Structure

```text
OnlineRetailRecommendation/
│── recommendation.py
│── README.md
```

---

## 📦 Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/OnlineRetailRecommendation.git
```

2. Navigate to the project folder:

```bash
cd OnlineRetailRecommendation
```

3. Install the required libraries:

```bash
pip install pandas scikit-learn
```

---

## ▶️ How to Run

Run the following command:

```bash
python recommendation.py
```

Enter a product name when prompted.

Example:

```text
Enter Product Name: Laptop
```

Example Output:

```text
Recommended Products for 'Laptop':

Monitor
Laptop Stand
Webcam
Mechanical Keyboard
Gaming Mouse
```

---

## 🧠 How It Works

1. Loads the product dataset.
2. Converts product categories into numerical values.
3. Creates feature vectors using category and price.
4. Calculates product similarity using Cosine Similarity.
5. Displays the top recommended products based on similarity.

---

## 📈 Future Improvements

* Use a real online retail dataset.
* Add customer purchase history.
* Implement collaborative filtering.
* Develop a web interface using Streamlit or Flask.
* Recommend products using Deep Learning.

---

## 👨‍💻 Author

**Aditya Panwar**

B.Tech CSE (AI/ML)

THDC Institute of Hydropower Engineering and Technology

---

## 📜 License

This project is open source and available for educational purposes.
