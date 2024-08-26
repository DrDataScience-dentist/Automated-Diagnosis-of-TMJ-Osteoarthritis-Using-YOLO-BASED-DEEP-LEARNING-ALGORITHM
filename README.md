
![1722607498610](https://github.com/user-attachments/assets/2d84864a-395d-4287-b756-b2224e2e551a)



# **TRAIN YOLOV8 OBJECT DETECTION ON A CUSTOM DATASET (DIAGNOSING TMJ OSTEOARTHRITIS)**

---
**!! HI GUYS**



I am **Balaganesh**, currently a house surgeon at **Sri Venkateswara Dental College**. In this tutorial iam going to show you how to train YOLOV8 on custom dataset of **TMJ osteoarthritis**


**Before you start**, if you encounter any issues or have any doubts, feel free to ping me on any of the social media platforms listed below. You can also provide your requirements in my GitHub repository.


[![GMAIL](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:drbalaganesh.dentist@gmail.com)
[![INSTAGRAM](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/_bala.7601/)
[![LINKDIN](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/drbalaganeshdentist/)
[![GITHUB](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DrDataScience-dentist/Automated-Diagnosis-of-TMJ-Osteoarthritis-Using-YOLO-BASED-DEEP-LEARNING-ALGORITHM)
---
## ⚠️ Disclaimer
I have created this notebook in [Kaggle](https://www.kaggle.com/) platform, I recommend to use kaggle for training this notebook snice it proivide 💪 **2 T4 GPU** but you can also use [Google Colab](https://colab.research.google.com/)

**REQUIREMENTS**
* LAPTOP OR PC
* DATASET
* [ROBOFLOW ACCOUNT](https://roboflow.com/)
* [KAGGLE](https://www.kaggle.com/) OR [COLAB](https://colab.research.google.com/)

**Use GPU Acceleration**
If you are running this notebook in Kaggle , navigate to `sidebar`  -> in the side bar search for  `session options` -> `accelerator` , set it to `GPU t4 x 2`, and then click `Turn on GPU T4 x 2`. This will ensure your notebook uses a GPU, which will significantly speed up model training times. In case of no side bar go to `View` -> `show sidebar`

If you are running this notebook in Google Colab, navigate to `Edit` -> `Notebook settings` -> `Hardware accelerator`, set it to `GPU`, and then click `Save`.


---

Creating a custom dataset can be a time-consuming and challenging task, often requiring dozens or even hundreds of hours to gather images, label them, and export them in the correct format. Thankfully, Roboflow simplifies and accelerates this process significantly. Let me guide you through it!

**First create a Roboflow account**
<div align="center">
  <img
    width="2000"
    src="attachment:cc0c7a6c-1781-4873-8537-a23fbdf6417b.png"
  >
    
**Create workspace**
    
    
<div align="center">
  <img
    width="2000"
    src="attachment:c72d1ea5-a14b-45e9-9c11-1d09e86dec9c.png"
  >
    
    
**Create Project**
    
    
<div align="center">
  <img
    width="2000"
    src="attachment:476b5217-8e2b-48e2-8888-65778fbadb8a.png"
  >
 
**Add class**
    
    
<div align="center">
  <img
    width="2000"
    src="attachment:9460f7da-23ac-4bc5-952c-2a104eaeb399.png"
  >
 
**Add images** by drag & drop or  add entire folder
    
    
<div align="center">
  <img
    width="2000"
    src="attachment:72dbccb0-09fa-48bc-bc6d-598af200f251.png"
  >
    
**Start annotating** use bounding box or polygon to annotate
    
    
<div align="center">
  <img
    width="2000"
    src="attachment:335af6b8-fdc0-4ff6-a0ff-3a39ad3deb8e.png"
  >    
 
**After annotation genrate dataset**
    Now that we have our images and annotations added, we can Generate a Dataset Version. When Generating a Version, you may elect to add preprocessing and augmentations. This step is completely optional, however, it can allow you to significantly improve the robustness of your model.
    
    
<div align="center">
  <img
    width="2000"
    src="attachment:b9b1a421-a745-4bc8-93af-592e3347148a.png"
  > 
 
**Exporting dataset**
  Once the dataset version is generated, we have a hosted dataset we can load directly into our notebook for easy training. Click `Export` and select the `YOLO v8` dataset format. copy below shown code which will be used later in this tutorial
    
<div align="center">
  <img
    width="2000"
    src="attachment:c4164854-8322-4a7f-a5a2-19cab6e77107.png"
  >
    
  ---
