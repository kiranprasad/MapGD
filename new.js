function call(){
	var img=document.getElementById('myimg');
	var src=img.src;
	window.open(src);  
}


function something()
{
  var selectpiece = document.getElementById("newSelection");
  var img=document.getElementById("myimg");
  //alert(selectpiece.selectedIndex);
  if(selectpiece.options[selectpiece.selectedIndex].getAttribute("id") == "1") 
  	{ 		
  		img.src="Astronomyand AstrophysicsReview!!.png";
  	}
  else if(selectpiece.options[selectpiece.selectedIndex].getAttribute("id") == "2") 
  	{
  		img.src="AstroJournal!!.png";
  	}
   else if(selectpiece.options[selectpiece.selectedIndex].getAttribute("id") == "3") 
  	{
  		img.src="MNRAS!!.png";
  	}
    else if(selectpiece.options[selectpiece.selectedIndex].getAttribute("id") == "4") 
  	{
  		img.src="icarus!!.png";
  	}
     else if(selectpiece.options[selectpiece.selectedIndex].getAttribute("id") == "5") 
  	{
  		img.src="NewAstroReviews!!.png";
  	}
    else if(selectpiece.options[selectpiece.selectedIndex].getAttribute("id") == "6") 
  	{
  		img.src="PasTP!!.png";
  	}
     else if(selectpiece.options[selectpiece.selectedIndex].getAttribute("id") == "7") 
  	{
  		img.src="ASCOM!!.png";
  	}
		
}
