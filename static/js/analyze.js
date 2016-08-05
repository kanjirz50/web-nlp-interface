var r;
$(function() {
  $("#btn-analyze").click(function(){
    $.ajax({
      type: "GET",
      url: "/api/analyzer",
      data: {
        "input_text": $("#input-text").val()
      },
      contentType: 'application/JSON',
      dataType : 'JSON',
      scriptCharset: 'utf-8',

      success: function(result){
        console.log("success");
        console.log(result);
        r = result;
        writeTable(result);
      },

      error: function(xhr, status, err) {
        console.log("error");
      }
    });
  });
});

function writeTable(result)
{
  $("#tbl-result tbody").html("");
  result.forEach(
    function(elem){
      $(
        "<tr>" +
        "<td>" + elem[0] + "</td>" +
        "<td>" + elem[1] + "</td>" +
        "</tr>"
      ).appendTo("#tbl-result tbody");
    }
  );
}
