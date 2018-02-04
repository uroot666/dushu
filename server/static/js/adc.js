jQuery(function(){
membertotalCount1();
});
function membertotalCount1(){
	var url = "/book/list/?num=all";
	jQuery.get(url,function(result){
			console.log(result);
			var list = JSON.parse(result);
			var list = list.data
			console.log(list);
		var member_total = $('#member_total');
			member_total.empty();
			for (var i = 0; i < list.length; i++) {
				var membertotal = list[i];
				var td1 = $('<td></td>');	
				var td2 = $('<td></td>');	
				var td3 = $('<td></td>');	
				var td4 = $('<td></td>');	
				var td5 = $('<td></td>');	
				var td6 = $('<td></td>');
				var tr =  $('<tr></tr>');
				td1.html(membertotal.title);
				td2.html(membertotal.author);
				td3.html(membertotal.publisher);
				td4.html(membertotal.pubdate);
				td5.html(membertotal.price);
				td6.html('未计算');
				
				tr.append(td1).append(td2).append(td3).append(td4).append(td5).append(td6);
				member_total.append(tr);	
			}
		
	});
	}
