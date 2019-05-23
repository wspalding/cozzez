var site_url;

$(function () 
{
  // Get Url from django
  var source = document.getElementById("hidden_url");
  site_url = source.innerHTML
  site_url = site_url.replace(/\s+/g,'')
  // source.style.display = "none";
});


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
