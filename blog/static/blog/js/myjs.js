$(document).ready(function(){
    $('p').attr('align', 'justify');
    $('h1').css('font-family', "'Gloria Hallelujah', cursive, serif");
    $(".button-collapse").sideNav();
    $( 'pre' ).addClass( 'prettyprint' );
    $( 'code' ).addClass( 'lang-py' );
    $( 'img' ).addClass( 'img-responsive' );

    var fileUrl = $('.content-text img').attr('src');
    console.log(fileUrl)
    if (fileUrl != undefined){
        var parts, ext = ( parts = fileUrl.split("/").pop().split(".") ).length > 1 ? parts.pop() : "";
        console.log(ext);
        if (ext != 'gif') {
            $( '.content-text img' ).addClass( 'materialboxed' );
        }
    }

    $('.materialboxed').materialbox();

    var jPM = $.jPanelMenu();
    jPM.on();
});