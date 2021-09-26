$(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});
    $('.parallax').parallax();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    $('.timepicker').timepicker({
        showClearBtn: true,
        i18n: {
            done: "Select",
            clear: "Clear",
            cancel: "Cancel"
        }
    });
  
  });