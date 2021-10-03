$(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});
    $('.parallax').parallax();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();
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
        twelveHour: false,
        i18n: {
            done: "Select",
            clear: "Clear",
            cancel: "Cancel"
        }
    });  

    

/*---price working on ON not OFF---*/
$( "#price_free" ).val("on").click(function() {
    $("#price_amount").css("display", "none");
});

$( "#price_free" ).val("off").click(function() {
    $("#price_amount").css("display", "visible");
});




/*-------

function priceSwitch() {
let price_freeOn = $("#price_free").val();

if (price_freeOn == "on") {
    $("#price_amount").css("display", "none"); //hidden price
  } else {
    $("#price_amount").css("display", "visible"); //price visible
  }
};





$( "#price_free" ).click(function() {
    if ("#price_free" == "on") {
        $("#price_amount").css("display", "none");
    } else {
        $("#price_amount").css("display", "visible")
    }
  });

  ---*/


    /*----validate select/div in forms - adapted from source Code Institute "Materialize Form Validation" lesson---*/
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #880e4f", "box-shadow": "0 1px 0 0 #880e4f" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(136, 14, 79)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
  
  });