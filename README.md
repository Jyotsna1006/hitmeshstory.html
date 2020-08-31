# hitmeshstory.html















<!doctype html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>hitmeshstory.html</title>
<script type="text/javascript"src="hitmeshstory.js">
  function hii(){
  var txtdisease=document.getElementByID("txtdisease");
  var username=txtdisease.value;
  var output=document.getElementByID("output");
  output.innerhtml="HIII"+username+" is a severe disease which anyone living carelessly can adopt,and is quite vulnerable";
  var txtcountry=document.getElementByID("txtcountry");
  var username=txtcountry.value;
  var output=document.getElementByID("output");
  output.innerhtml="Many asian and European big countries including"+username+" is a worst prey ";
  var textdiseasesymptom=document.getElementByID("txtdiseasesymptom");
  var username=txtdiseasesymptom.value;
  var output=document.getElementByID("output");
  output.innerhtml="cough,sneeze, nausea, weak digestion,headache and"+username+are its common symptoms to be cared;
</script>
  <body>
    <h1 align="centre">know it!!!</h1>
    <form action="">
      <fieldset>
        <label for="txtdisease">name a disease</label>
        <input type="text" id="txtdisease"/>

<label for="txtcountry">name a country</label>
        <input type="text" id="txtcountry"/>

<label for="charnumber">put a number</label>
        <input type="character" id="charnumber"/>



<label for="txtdiseasesymptom">name a disease symptom</label>
        <input type="text" id="txtdiseasesymptom"/>









 



    <button onclick=" hii() type="button">narrate whole lot of ur disease idea
</button>


    </fieldset>
    <div id="output"></div>
    </form>
    </body>
    </html>


