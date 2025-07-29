# 🧠 DigitNet — Handwritten Digit Recognition from Scratch

A simple neural network built **from scratch in Python using NumPy**, trained on the MNIST dataset to recognize handwritten digits (0–9).

> 🔢 Achieves over **90% accuracy** on the MNIST test set  
> 🧮 Implements feedforward, backpropagation, and stochastic gradient descent (SGD) from first principles  
> 🚫 No machine learning libraries like TensorFlow or PyTorch — everything is handcrafted

---

## 📊 Sample Training Output

```
Epoch 0: 8423 / 10000
Epoch 1: 8762 / 10000
...
Epoch 29: 9065 / 10000
```

---

## 🛠 Features

- Neural network implementation from scratch:
  - Feedforward propagation
  - Backpropagation
  - Mini-batch stochastic gradient descent (SGD)
- Lightweight and educational
- Uses NumPy for matrix operations
- Custom `mnist_loader.py` to load the dataset

---

## 🧪 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/kebal7/digit-net.git
cd digit-net
```

### 2. Set up Python environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install numpy
```

### 3. Train the model

```bash
python3 src/main.py
```

You should see accuracy improving every epoch.

---

## 📁 Project Structure

```
digitnet/
├── data/
│   └── test/
│       └── digit.png       # Place your test image here
├── model/
│   └── digit_model.npz     # Saved trained model
├── src/
│   ├── main.py             # Entry point for training
│   ├── network.py          # Neural network implementation
│   ├── mnist_loader.py     # MNIST data loader
│   └── test_image.py       # Script to test your image
├── README.md               # Project documentation            # Project documentation
```

---

## 📚 What I Learned

This project helped me understand:

- How neural networks learn from data
- Forward and backward pass mechanics
- How gradients flow and update weights
- Matrix math using NumPy
- Importance of clean architecture and modular code

---

## 🚀 Future Plans (WIP)

- [ ] Add a simple web interface with Flask
- [ ] Allow image upload or drawing with a brush
- [ ] Show prediction results with confidence
- [ ] Save and load trained weights for reuse
- [ ] Host it online as a demo

---

## 🙏 Credits

Based on concepts from  
📘 *Neural Networks and Deep Learning* by [Michael Nielsen](http://neuralnetworksanddeeplearning.com/)

---

## 👨‍💻 Author

**Kebal Badal**  
AI Student | Builder | Explorer  
[GitHub](https://github.com/kebal7) 
