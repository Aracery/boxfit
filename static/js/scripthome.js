(function(){
    
    var $window = $(window);
    var $header = $('header');

    var realheader = document.getElementById('realheader');
    var realheaderimage = document.getElementById('realheaderimage');

    var headerimagefracheight = (realheaderimage.clientHeight/40).toString() + "px";

    realheader.style.setProperty("box-shadow", "0 " + headerimagefracheight + " " + headerimagefracheight + " #aa0000ff");

    $window.on('resize', function(e){
    var headerimagefracheight = (realheaderimage.clientHeight/40).toString() + "px";
    realheader.style.setProperty("box-shadow", "0 " + headerimagefracheight + " " + headerimagefracheight + " #aa0000ff");
    });

// 
    $window.on('scroll', function(e){
    if ($window.scrollTop() < (realheaderimage.clientHeight-realheader.clientHeight)-realheaderimage.clientHeight/35){
        realheader.style.setProperty("box-shadow", "0 " + headerimagefracheight + " " + headerimagefracheight + " #aa0000ff");
    } else {
        realheader.style.setProperty("box-shadow", "none");
    }
    });
}());
