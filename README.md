![Moose-logo](Images/Moose-logo.png)

![](https://komarev.com/ghpvc/?username=QIMP-Team&color=blueviolet&style=for-the-badge)[![image](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/playlist?list=PLZQERorVWrbcG4AMkDQ9KrL_Rr77D1-6k) [![image](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/9uTHYhWCA5) [![image](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/qimp/) [![Share on Twitter](https://img.shields.io/badge/Twitter-share%20on%20twitter-blue?logo=twitter&style=for-the-badge)](https://twitter.com/intent/tweet?text=Check%20out%20MOOSE%20(Multi-organ%20objective%20segmentation%20:https://github.com/QIMP-Team/MOOSE)%20a%20data-centric%20AI%20solution%20that%20generates%20multilabel%20organ%20segmentations%20to%20facilitate%20systemic%20TB%20whole-person%20research.) 


## MOOSE 2.0 🫎 - Leaner. Meaner. Stronger 💪

Unveiling a new dimension in 3D medical image segmentation: MOOSE 2.0 🚀

Crafted meticulously from the core principles of data-centric AI, MOOSE 2.0 is our response to the demands of both preclinical and clinical imaging. 

✨ It's Leaner: We've hacked away the fluff and made MOOSE 2.0 leaner than ever before. This bad boy doesn't need heavy-duty computing. With less than 32GB of RAM, compatibility across OS, and the flexibility to work with or without NVIDIA GPUs, MOOSE 2.0 fits right into any environment. 🔬

💥 It's Meaner: Our engineers have poured their hearts and souls into building this beast from scratch. With the speed clocking 5x faster than its predecessor, MOOSE 2.0 cuts through the noise and gets down to business instantly. It serves up a range of segmentation models designed for both clinical and preclinical settings. No more waiting, no more compromises. It's Mean Machine time! ⚡

🔥 It's Stronger: MOOSE 2.0 is powered by the sheer strength of Data-centric AI principles. With a whopping 2.5k datasets, that's x times more data than our first model, we're packing a punch. MOOSE 2.0 comes with the strength and knowledge gained from an array of data that's simply unparalleled. The result? Better precision, improved outcomes, and a tool you can trust. 💼

Accommodating an array of modalities including PET, CT, and MRI, MOOSE 2.0 stands at the cusp of a paradigm shift. It’s not just an upgrade; it’s our commitment to making MOOSE 2.0 your go-to for segmentation tasks.

Join us as we embark on this journey.

## Installation Guide 🛠️

Available on Windows, Linux, and MacOS, the installation is as simple as it gets. Follow our step-by-step guide below and set sail on your journey with MOOSE 2.0.

## For Linux and MacOS 🐧🍏

1. First, create a Python environment. You can name it to your liking; for example, 'moose-env'.
   ```bash
   python3 -m venv moose-env
   ```

2. Activate your newly created environment.
   ```bash
   source moose-env/bin/activate  # for Linux
   source moose-env/bin/activate  # for MacOS
   ```

3. Install MOOSE 2.0.
   ```bash
   pip install moosez
   ```

Voila! You're all set to explore with MOOSE 2.0.

## For Windows 🪟

1. Create a Python environment. You could name it 'moose-env', or as you wish.
   ```bash
   python -m venv moose-env
   ```

2. Activate your newly created environment.
   ```bash
   .\moose-env\Scripts\activate
   ```

3. Go to the PyTorch website and install the appropriate PyTorch version for your system. **!DO NOT SKIP THIS!**

4. Finally, install MOOSE 2.0.
   ```bash
   pip install moosez
   ```

There you have it! You're ready to venture into the world of 3D medical image segmentation with MOOSE 2.0.

Happy exploring! 🚀🔬

## Usage Guide 📚

Embarking on your journey with MOOSE 2.0 is straightforward and easy. Our command-line tool requires only two arguments: the directory path where your subject images are stored, and the segmentation model name you wish to use. Here's how you can get started:

```bash
moosez -d <path_to_image_dir> -m <model_name>
```

Here `<path_to_image_dir>` refers to the directory containing your subject images and `<model_name>` is the name of the segmentation model you intend to utilize. 

For instance, to perform clinical CT organ segmentation, the command would be:

```bash
moosez -d <path_to_image_dir> -m clin_ct_organs
```

In this example, 'clin_ct_organs' is the segmentation model name for clinical CT organ segmentation.

And that's it! With just one command, you're all set to explore the new horizons of 3D medical image segmentation with MOOSE 2.0.

Need assistance along the way? Don't worry, we've got you covered. Simply type:

```bash
moosez -h
```

This command will provide you with all the help and additional information you might need.

Happy Segmenting! 🎯🚀

## 🦌 MOOSE: An ENHANCE-PET Project

![Alt Text](https://github.com/QIMP-Team/MOOSE/blob/main/Images/DALL·E%202022-11-01%2018.13.35%20-%20a%20moose%20with%20majestic%20horns.png)
<p align="right">Above image generated by dall-e</p>
