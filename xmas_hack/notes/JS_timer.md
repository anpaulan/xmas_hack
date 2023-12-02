This is how you set up timer on when the reveal of secret santa is available
For this you will need Javascript and you can redirect to any page you wish with the following:

JavaScript Redirect Methods

  window.location = "http://stackoverflow.com";

  window.location.href = "http://stackoverflow.com";

  window.location.assign("http://stackoverflow.com");

  window.location.replace("http://stackoverflow.com");

'''

actual JS code
if (time() < strtotime("12/24/2023  6:00PM"))
{
    //redirect to current
    header("Location : http://xmas_hack.com/https://i5.walmartimages.com/seo/The-Grinch-Who-Stole-Christmas-Grinch-I-Need-Coffee-Hanging-Sign-16-5-inches-Tall-MDF-Green_7687d2ce-52ad-4e80-97f8-b7e1c8c4ddf1.2b0ee4f4425746a36356039c4b7b2a35.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF"); 
    exit;
}
    elseif(time() > strtotime("12/24/2023  6:00PM")){

    //redirect to new
    header("Location : http://website.com/reveal");
    exit;
}