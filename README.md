# Pix2Struct-Conversion
# RESULTS
---

## SIZE


1.   HugginFace Model : 1.13 Gb

There are 2 methods to convert to onnx </br>
* !optimum-cli export onnx  --model google/pix2struct-docvqa-base model/

       *   encoder_model.onnx : 350.53 Mb
       *   decoder_model.onnx : 726.87 Mb
       *   decoder_model_merged.onnx : 727.2 Mb
       *   decoder_with_past_model.onnx : 672.83 Mb

       ERROR-> logits: max diff = 2.6702880859375e-05.


*  !optimum-cli export onnx --model  google/pix2struct-docvqa-base --task visual-question-answering model/

       *  Generates the same models  

       ERROR-> logits: max diff = 3.814697265625e-05.   








  
      







