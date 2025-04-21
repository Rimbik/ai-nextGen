see# Run LLaMA Offline on Your PC

**LLaMA** is a GPT-equivalent model (developed by Meta/Facebook), part of the open-source large language models (LLMs) by Meta AI.

---

## 🤔 What Will You Get From This?

**Overview:**  
Once you complete the setup, you’ll be able to run the LLaMA model offline on your local PC. You'll effectively have a ChatGPT-style prompting system running locally.

There are various **LLaMA** models available online. Some require high-end hardware (like dual GPUs with 80GB RAM), but there are also lighter models that can run on machines with no GPU and only 4GB RAM.

---

## 🧰 Prerequisites

- A Linux PC/Laptop  
- Minimum 4GB RAM (Reported to work)  
- A decent CPU (Even Raspberry Pi with 4GB has been reported to work)  
- Basic C++ knowledge (Optional)  
- Basic Linux skills (Installing packages, running commands)

---

## 🚀 Let's Start

> ⚠️ This setup is influenced by a YouTube tutorial. Please watch the video first to get a sense of the overall process:  
> [YouTube Link](https://www.youtube.com/watch?v=EgoHtsOgZhY&t=71)

### Step-by-Step Instructions:

1. **Watch the YouTube video.**
2. **Clone the repository.**
3. **Compile the project using `make` or `cmake`.**
4. **Download the LLaMA model.**
5. **Place the model in your cloned folder.**
6. **Run commands to get it working.**

---

## 📚 References

- **LLaMA model downloads:**  
  [https://www.llama.com/llama-downloads/](https://www.llama.com/llama-downloads/)

- **Source code repo to clone:**  
  [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

- **Additional scripts:**  
  [convert-pth-to-ggml.py](https://github.com/cornelk/llama-go/blob/go/convert-pth-to-ggml.py)

---

## 🧑‍💻 Running Steps in Detail

### Step 1: Watch the Video

Watch this YouTube video to get started:  
[https://www.youtube.com/watch?v=EgoHtsOgZhY&t=71](https://www.youtube.com/watch?v=EgoHtsOgZhY&t=71)

---
Start making your hand dirty ..
### Step 2: Clone the Repository

```bash
mkdir llama
cd llama
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
```

Make sure you use `git clone` (not downloading the ZIP).

---

the everest camp 3
### Step 3: Compile the Project
(am in linux mint)
Use:

```bash
make
```

If `make` fails, try:

```bash
cmake .
```

> ⚠️ You might face errors during compilation due to missing packages. Install the suggested dependencies using `sudo apt-get` or `pip`.  
> This step can be the hardest due to C++ build issues. Don't worry—just ask for help if you get stuck!

---

### Step 4: Download the LLaMA Model

- Visit: [https://www.llama.com/llama-downloads/](https://www.llama.com/llama-downloads/)
- Register, fill out the form, and download a model.
- Scroll to **"Previous Language & Safety Models"** to get the low-end "LLaMA 2" model that runs on basic hardware.
- The model is ~13GB in size and is usually saved in your `/home/` directory.

> ![LLaMA 2 Model](images/llama2_model.png)

---

### Step 5: Move Model to Project Folder

1. Go to your cloned project directory.
2. Paste the downloaded model into the `models/` folder.

To check available public models:

```bash
llama model show
```

> ![LLaMA Models](images/llamaModelsAll.png)

---

### Step 6: Run the Model

1. Download and place the required script in your project root:

   [convert-pth-to-ggml.py](https://github.com/cornelk/llama-go/blob/go/convert-pth-to-ggml.py)

2. Install dependencies:

```bash
sudo python3 -m pip install torch numpy sentencepiece
```

3. Convert the 7B model to GGML FP16 format:

```bash
python3 convert-pth-to-ggml.py models/Llama-2-7b 1
```

- Use `0` or `1` as the second argument based on the model.
- Ensure correct folder names.

> ⚠️ This step may crash on low-end hardware. If using a machine with 2GB RAM (e.g., Acer Celeron), it may not complete.
image just before it crashes in full 2 gb ram
> ![crashed_on_convert](https://github.com/user-attachments/assets/27be86b5-6a4c-45ff-90ed-11e8c349e572)

4. Quantize the model to 4-bit:

```bash
python3 quantize.py 7b
```
You’re 98% done! For the final steps, refer to the video tutorial again.
[https://www.youtube.com/watch?v=EgoHtsOgZhY&t=71](https://www.youtube.com/watch?v=EgoHtsOgZhY&t=71)

**Conclusion:**
Since I have been crashed with my 2GB RAM in a celeron Laptop to run the model, spinning up a new system with Limux that has higher RAM. 
Untill then Best Of Luck!


---

## ✅ Additional Resources

- [Meta's LLaMA GitHub](https://github.com/meta-llama/llama-models/blob/main/README.md)
- [LLaMA.cpp main repo](https://github.com/ggml-org/llama.cpp)
- [LLaMA.cpp README](https://github.com/ggml-org/llama.cpp/blob/master/README.md)
