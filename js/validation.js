
$(document).ready(function() {
$("#basic-form").validate({
rules: {
Name : {
required: true,
minlength: 3
},



Sibsp : {
required: true,
number: true
},

Age: {
required: true,
number: true
},


Parch: {
required: true,
number: true
},



Gender: {
required: true

},



Cost : {
required: true,
number: true,
min: 0,
max: 550
},



Class : {
required: true,
number: true,
min: 1,
max: 3
},

},
  messages: {
    Name: "Please specify your name",
    Gender: {
      required: "Please Enter Your Gender"
      
    }
  }
});


});


