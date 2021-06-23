function category_open(){
    document.getElementById('category_open').style.display='none';
    document.getElementById('category_close').style.display='inline';
    document.getElementById('categories').style.display='inline';
}

function category_close(){
    document.getElementById('category_open').style.display='inline';
    document.getElementById('category_close').style.display='none';
    document.getElementById('categories').style.display='none';
}

function show_more()
{
    document.getElementById("more_news").style.display='inline';
    document.getElementById("load_more").style.display='none';
}

function dark_theme()
{
    document.getElementById("light").style.display="none"
    document.getElementById("dark").style.display="inline"
}

function light_theme()
{
    document.getElementById("light").style.display="inline"
    document.getElementById("dark").style.display="none"
}
