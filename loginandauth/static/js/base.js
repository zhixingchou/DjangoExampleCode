//此函数用于checkbox的全选和反选
var checked=false;
function check_all(form) {
    var checkboxes = document.getElementById(form);
    if (checked == false) {
        checked = true
    } else {
        checked = false
    }
    for (var i = 0; i < checkboxes.elements.length; i++) {
        if (checkboxes.elements[i].type == "checkbox") {
            checkboxes.elements[i].checked = checked;
        }
    }
}

function checkAll(id, name){
    var checklist = document.getElementsByName(name);
    if(document.getElementById(id).checked)
        {
        for(var i=0;i<checklist.length;i++)
        {
          checklist[i].checked = 1;
        }
    }else{
        for(var j=0;j<checklist.length;j++)
        {
         checklist[j].checked = 0;
        }
    }
}

//提取指定行的数据，JSON格式
function GetRowData(row){
    var rowData = {};
    for(var j=0;j<row.cells.length; j++) {
        name = row.parentNode.rows[0].cells[j].getAttribute("Name");
        if (name) {
            var value = row.cells[j].getAttribute("Value");
            if (!value) {
                value = row.cells[j].innerHTML;
            }
            rowData[name] = value;
        }
    }
    return rowData;
}

//此函数用于在多选提交时至少要选择一行
function GetTableDataBox() {
    var tabProduct = document.getElementById("editable");
    var tableData = new Array();
    var returnData = new Array();
    var checkboxes = document.getElementById("contents_form");
    var id_list = new Array();
    len = checkboxes.elements.length;
    for (var i=0; i < len; i++) {
        if (checkboxes.elements[i].type == "checkbox" && checkboxes.elements[i].checked == true && checkboxes.elements[i].value != "checkall") {
            id_list.push(i);
         }
        }
    console.log(id_list);
    for (i in id_list) {
        console.log(tabProduct);
        tableData.push(GetRowData(tabProduct.rows[id_list[i]]));
    }

    if (id_list.length == 0){
        alert('请至少选择一行！');
    }
    returnData.push(tableData);
    returnData.push(id_list.length);
    return returnData;
}

function move(from, to, from_o, to_o) {
    $("#" + from + " option").each(function () {
        if ($(this).prop("selected") == true) {
            $("#" + to).append(this);
            if( typeof from_o !== 'undefined'){
                $("#"+to_o).append($("#"+from_o +" option[value='"+this.value+"']"));
            }
        }
    });
}

function move_left(from, to, from_o, to_o) {
    $("#" + from + " option").each(function () {
        if ($(this).prop("selected") == true) {
            $("#" + to).append(this);
            if( typeof from_o !== 'undefined'){
                $("#"+to_o).append($("#"+from_o +" option[value='"+this.value+"']"));
            }
        }
        $(this).attr("selected",'true');
    });
}

//function move_all(from, to) {
//    $("#" + from).children().each(function () {
//        $("#" + to).append(this);
//    });
//}
//

//function selectAllOption(){
//         var checklist = document.getElementsByName ("selected");
//            if(document.getElementById("select_all").checked)
//            {
//            for(var i=0;i<checklist.length;i++)
//            {
//              checklist[i].checked = 1;
//            }
//            }else{
//            for(var j=0;j<checklist.length;j++)
//            {
//             checklist[j].checked = 0;
//            }
//            }
//
//        }


function selectAll(){
    // 选择该页面所有option
    $('option').each(function(){
        // $(this)是一个JQuery对象;JQuery拥有attr()方法可以get/set DOM对象的属性
        // 使用JQuery的好处是它包裝了各种浏览器版本对DOM对象的操作，因此统一使用$(this)而不再用this应该是比较不错的选择。(this其实是一个Html 元素)
        // by zhouzx
        $(this).attr('selected', true)
    })
}


//
//function move_all(from, to){
//    $("#"+from).children().each(function(){
//        $("#"+to).append(this);
//    });
//}

//function commit_select(form_array){
//    $('#{0} option'.format(form_array)).each(function(){
//        $(this).prop('selected', true)
//        })
//}

function getIDall() {
    var check_array = [];
    $(".gradeX input:checked").each(function () {
        var id = $(this).attr("value");
        // push() 方法可向数组的末尾添加一个或多个元素，并返回新的长度。
        check_array.push(id);
    });
    // 指定要使用的分隔符。如果省略该参数，则使用逗号作为分隔符。
    return check_array.join(",");
}