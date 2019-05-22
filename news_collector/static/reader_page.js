let site_url = document.getElementById("my_url");


$(function () 
{
  // Grab the template script
  var source = document.getElementById("webpage_template").innerHTML;

  // Compile the template
  var template = Handlebars.compile(source);

  // console.log(template)
  // Define our data object
  var context = {
  	website: "this works",
  };
  // console.log(context)
  // Pass our data to the template
  var html = template(context);
  // console.log(html)
  // Add the compiled html to the page
  $('.webpage_results').html(html);
});


function test() 
{
	// body...
	// Grab the template script
  var source = document.getElementById("webpage_template").innerHTML;

  // Compile the template
  var template = Handlebars.compile(source);

  console.log(site_url)
  // Define our data object
  var context = {
  	website: "testing",
  };
  var html = template(context);

  $('.search_results').html(html);
  return false;
}

function display_website()
{
	var url = "https://youtube.com"
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
