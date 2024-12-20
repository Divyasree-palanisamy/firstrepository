 function validateName(){
  let  nameElement = document.getElementById("name");
 
   let nameErrorElement = document.getElementById('name-error');
    if(nameElement.value.trim()===""){
   
      nameErrorElement.innerText = "Enter the name";
      return false;
   }else{
        nameErrorElement.innerText ="";
        return true;
    }
}
function validateCourse(){
    let courseElement = document.getElementById("course");


    let courseErrorElement = document.getElementById('course-error');
    if(courseElement.value.trim()===""){
        courseErrorElement.innerHTML = "Select a course";
        return false;
    }else{
        courseErrorElement.innerHTML = "";
        return true;
    }
  
}
function validateDepartment(){
  let departmentElement = document.getElementById("department");

  let departmentErrorElement = document.getElementById('department-error');
  if(departmentElement.value.trim()===""){
      departmentErrorElement.innerHTML = "Select a department";
      return false;
  }else{
      departmentErrorElement.innerHTML = "";
      return true;
  }

}
function validateDateOfBirth(){
  let dateOfBirthElement = document.getElementById("dob");

  let dobErrorElement = document.getElementById('dob-error');
  if(dateOfBirthElement.value ==""){
      dobErrorElement.innerHTML = "Select a date";
      return false;
  }else{
      dobErrorElement.innerHTML = "";
      return true;
  }

}


function validateSemester(){
  let semesterElement = document.getElementById("semester");

    let semesterErrorElement = document.getElementById('semester-error');
    let semester = parseInt(semesterElement.value);
    if(semesterElement.value == "" || semester<1 || semester>8){
  
        semesterErrorElement.innerText = "Enter the valid semester";
        return false;
   }else{
        semesterErrorElement.innerText ="";
        return true;
    }
}
function validateEmail(){
  let emailElement = document.getElementById("email");

  let email = emailElement.value.trim();
  let emailErrorElement = document.getElementById('email-error');
  const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  let isEmailValid = emailRegex.test(email)
  if(email=="" || !isEmailValid){
    emailErrorElement.innerText = "Enter valid mail";
    return false;
  }else{
    emailErrorElement.innerText = "";
    return true;

  }
  }
  function validateGender(){
    let genderErrorElement = documnent.getElementById('gender-error');
    let genderRadioButtons = document.getElementsByName('gender');
    let genderSelected = false;
    for (let gender of genderRadioButtons){
      if(gender.checked ==true){
        genderSelected = true;
        break;
      }
    } 
    if(!genderSelected){
      genderErrorElement.innerText = "Select a gender";
      return false;
    } else{
      genderErrorElement.innerText = "";
      return true;

    }
  }

function validateForm(){
  let errorCount = 0;
  if(!validateName()){
    errorCount++;
  }
  if(!validateEmail()){
    errorCount++;
  }
  if(!validateDateOfBirth()){
    errorCount++;
  }
  if(!validateGender()){
    errorCount++;
  }
  if(!validateCourse()){
    errorCount++;
  }
  if(!validateDepartment()){
    errorCount++;
  }
  if(!validateSemester()){
    errorCount++;
  }
  return errorCount==0;
}

function submitForm (){
  if(validateForm()){
    window.location.href = "grid.html";
  }
}





    





