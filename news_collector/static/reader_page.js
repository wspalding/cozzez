var site_url;
var today;

//recieve site url from server
$(function () 
{
  // Get Url from django
  var source = document.getElementById("hidden_url");
  site_url = source.innerHTML
  site_url = site_url.replace(/\s+/g,'') 
  // source.style.display = "none";
  //get_websites() 
  
});


//add date scroller to page
$(function()
{
	var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ];
	var scroller = document.getElementById("scroll_menu");
	var num_days = 14
	today = new Date();
	// console.log(today)
	DotW = 7; //today.getDay();
	for (var i = 0; i < num_days; i++) 
	{
		var current_day = new Date()
		current_day.setDate(today.getDate() + i - DotW)
		// console.log(current_day)
		var date = months[current_day.getMonth()] + " " + current_day.getDate()  + ", " + current_day.getFullYear();
		var url_date = "" + (current_day.getMonth() + 1) + current_day.getDate() + current_day.getFullYear();
		// console.log(url_date)
		// console.log(date)
		if(i == DotW)
		{
			scroller.innerHTML += "<a href=/" + url_date + ' class="current_day">' + date + "</a>";
		}
		else
		{
			scroller.innerHTML += "<a href=/" + url_date + ' class="not_current_day">' + date + "</a>";
		}
		
	}

	var source = document.getElementById("protest_post_template").innerHTML;
	var temp = Handlebars.compile(source);
	for (var i = 0; i < 10; i++) 
	{
		var context = {"number": i};
		document.getElementById("content").innerHTML += temp(context);
	}
	
});


//open login window
function login_signup()
{
	var modal = document.getElementById("login_modal");
	modal.style.display = "block";
	window.onclick = function(event) 
	{
		if (event.target == modal) 
		{
			modal.style.display = "none";
		}
	}
	// console.log("login_signup");
}

function login()
{
	return false;
}

function signup()
{
	return false;
}


function get_websites() 
{
	// body...
	var url = site_url + 'requests/news_links/test'
	console.log(url)
	$.ajax({
		url: url,
		type: "GET",
		contentType: 'application/json',
	    // data: json,
	    // dataType: 'json',
	    cache: false,
		success: function(result){
			console.log("result: ");
			console.log(result);
			// Grab the template script
			var source = document.getElementById("list_template").innerHTML;
			// Compile the template
			var template = Handlebars.compile(source);
			// Define our data object
			search_term = document.getElementById("search_bar").value;
			for (var i = result.links.length - 1; i >= 0; i--) 
			{
				if(!result.links[i].includes(search_term))
				{
					result.links.splice(i,1);
				}
				
			}

			var context = {
			  	list: result.links,
			  };
			var html = template(context);

			$('.search_results').html(html);
			return false;
		},
		error: function(error){
			console.log("error: ");
			console.log(error);
			var context = {
			  	website: error,
			  };
			 return false;
		}
	})
  return false;
}


function display_website()
{
	var url = site_url
	console.log(site_url)
	$.ajax({
		url: url,
		type: "GET",
		success: function(result){
			var source = document.getElementById("webpage_template").innerHTML;
			// Compile the template
			var template = Handlebars.compile(source);
			console.log(result)
			// Define our data object
			var context = {
				website: result,
			};
			// console.log(context)
			// Pass our data to the template
			var html = template(context);
			// console.log(html)
			// Add the compiled html to the page
			$('.webpage_results').html(html);
		},
		error: function(error){
			var source = document.getElementById("webpage_template").innerHTML;
			// Compile the template
			var template = Handlebars.compile(source);
			console.log(error)
			// Define our data object
			var context = {
				website: error,
			};
			// console.log(context)
			// Pass our data to the template
			var html = template(context);
			// console.log(html)
			// Add the compiled html to the page
			$('.webpage_results').html(html);
		}
	})
	return false;
}





// sidebar
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

