
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
![Screenshot 2024-08-26 215250](https://github.com/user-attachments/assets/71ec7f7d-10a1-479a-8c15-bd143d6adfac)

    
**Create workspace**
    
    

![Screenshot 2024-08-26 215502](https://github.com/user-attachments/assets/3e1bec68-03a0-4f14-97cf-a26b4fab1365)

    
**Create Project**
    
 
**Add class**
    

 
**Add images** by drag & drop or  add entire folder
    
    

    
**Start annotating** use bounding box or polygon to annotate
    

 
**After annotation genrate dataset**
    Now that we have our images and annotations added, we can Generate a Dataset Version. When Generating a Version, you may elect to add preprocessing and augmentations. This step is completely optional, however, it can allow you to significantly improve the robustness of your model.
    
    

 
**Exporting dataset**
  Once the dataset version is generated, we have a hosted dataset we can load directly into our notebook for easy training. Click `Export` and select the `YOLO v8` dataset format. copy below shown code which will be used later in this tutorial
    

    
  ---
