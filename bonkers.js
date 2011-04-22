var myDomain = document.domain;
var cgiURL;
var xmlRequest;

function play(val) {
    //alert(val);
    xmlRequest = new XMLHttpRequest();
	cgiURL="http://" + myDomain + "/cgi-bin/start-chrome.py?"+val;
	//alert(cgiURL);
	xmlRequest.open("GET", cgiURL, true);
	xmlRequest.send(null);
}
	
