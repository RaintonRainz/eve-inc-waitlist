function eveui_urlify(dna){return"https://o.smium.org/loadout/dna/"+encodeURI(dna)}function eveui_autocomplete_endpoint(str){return"https://zkillboard.com/autocomplete/typeID/"+encodeURI(str)+"/"}function eveui_new_window(){var eveui_window=$('\n\t\t<span class="eveui_window" style="position: fixed">\n\t\t\t<div class="eveui_title">&nbsp;</div>\n\t\t\t<span class="eveui_icon eveui_close_icon" />\n\t\t\t<span class="eveui_scrollable">\n\t\t\t\t<span class="eveui_content">\n\t\t\t\t\tLoading...\n\t\t\t\t</span>\n\t\t\t</span>\n\t\t</span>\n\t\t');return eveui_window.css("z-index",eveui_zindex++),eveui_window.css("left",eveui_x+10),eveui_window.css("top",eveui_y-10),eveui_window}function eveui_mark(mark){console.log("eveui: "+mark+" "+performance.now())}function eveui_generate_fit(dna,eveui_name){function item_rows(fittings,slots_available){var html="",slots_used=0;for(var item_id in fittings)slots_used+=fittings[item_id],html+=slots_available?'\n\t\t\t\t\t<tr class="copy_only">\n\t\t\t\t\t<td>\n\t\t\t\t\t\t'+(eveui_item_cache[item_id].name+"<br />").repeat(fittings[item_id])+'\n\t\t\t\t\t<tr class="nocopy" data-eveui-itemid="'+item_id+'">\n\t\t\t\t\t\t<td style="background-image: url(https://imageserver.eveonline.com/Type/'+item_id+'_32.png)" class="eveui_icon eveui_item_icon" />\n\t\t\t\t\t\t<td class="eveui_numeric">'+fittings[item_id]+"\n\t\t\t\t\t\t<td>"+eveui_item_cache[item_id].name+"\n\t\t\t\t\t":'\n\t\t\t\t\t<tr class="copy_only">\n\t\t\t\t\t<td>\n\t\t\t\t\t\t'+eveui_item_cache[item_id].name+" x"+fittings[item_id]+'\n\t\t\t\t\t<tr class="nocopy" data-eveui-itemid="'+item_id+'">\n\t\t\t\t\t\t<td style="background-image: url(https://imageserver.eveonline.com/Type/'+item_id+'_32.png)" class="eveui_icon eveui_item_icon" />\n\t\t\t\t\t\t<td class="eveui_numeric">'+fittings[item_id]+"\n\t\t\t\t\t\t<td>"+eveui_item_cache[item_id].name+"\n\t\t\t\t\t",html+='\n\t\t\t\t<td class="eveui_icon" />\n\t\t\t\t<td data-itemid="'+item_id+'" class="eveui_icon eveui_info_icon" />\n\t\t\t\t',eveui_allow_edit&&(html+='\n\t\t\t\t\t<td class="eveui_icon eveui_plus_icon" />\n\t\t\t\t\t<td class="eveui_icon eveui_minus_icon" />\n\t\t\t\t\t<td class="eveui_icon eveui_more_icon" />\n\t\t\t\t\t');return"undefined"!=typeof slots_available&&(slots_available>slots_used&&(html+='\n\t\t\t\t\t<tr class="nocopy">\n\t\t\t\t\t\t<td class="eveui_icon eveui_item_icon" />\n\t\t\t\t\t\t<td class="eveui_numeric">'+(slots_available-slots_used)+"\n\t\t\t\t\t\t<td>Empty\n\t\t\t\t\t",eveui_allow_edit&&(html+='<td class="eveui_more_icon" />')),slots_used>slots_available&&(html+='\n\t\t\t\t\t<tr class="nocopy">\n\t\t\t\t\t\t<td class="eveui_icon eveui_item_icon" />\n\t\t\t\t\t\t<td class="eveui_numeric">'+(slots_available-slots_used)+"\n\t\t\t\t\t\t<td>Excess\n\t\t\t\t\t")),html}var high_slots={},med_slots={},low_slots={},rig_slots={},subsystem_slots={},other_slots={},items=dna.split(":"),ship_id=parseInt(items.shift()),ship=eveui_item_cache[ship_id];for(var i in ship.dogma.attributes){var attr=eveui_item_cache[ship_id].dogma.attributes[i];"hiSlots"==attr.attribute.name?ship[attr.attribute.name]=attr.value:"medSlots"==attr.attribute.name?ship[attr.attribute.name]=attr.value:"lowSlots"==attr.attribute.name?ship[attr.attribute.name]=attr.value:"rigSlots"==attr.attribute.name?ship[attr.attribute.name]=attr.value:"maxSubSystems"==attr.attribute.name&&(ship[attr.attribute.name]=attr.value)}outer:for(var item in items)if(0!=items[item].length){var match=items[item].split(";"),item_id=match[0],quantity=parseInt(match[1]);for(var i in eveui_item_cache[item_id].dogma.effects){if("hiPower"==eveui_item_cache[item_id].dogma.effects[i].effect.name){high_slots[item_id]=quantity;continue outer}if("medPower"==eveui_item_cache[item_id].dogma.effects[i].effect.name){med_slots[item_id]=quantity;continue outer}if("loPower"==eveui_item_cache[item_id].dogma.effects[i].effect.name){low_slots[item_id]=quantity;continue outer}if("rigSlot"==eveui_item_cache[item_id].dogma.effects[i].effect.name){rig_slots[item_id]=quantity;continue outer}if("subSystem"==eveui_item_cache[item_id].dogma.effects[i].effect.name){subsystem_slots[item_id]=quantity;continue outer}}other_slots[item_id]=quantity}var html="";return html+='\n\t\t<div class="eveui_fit_header" data-eveui-itemid="'+ship_id+'">\n\t\t<span style="background-image: url(https://imageserver.eveonline.com/Type/'+ship_id+'_32.png)" class="eveui_icon eveui_ship_icon" />\n\t\t<span class="eveui_flexgrow">\n\t\t\t<span class="eveui_startcopy" />['+eveui_item_cache[ship_id].name+',\n\t\t\t<a target="_blank" href="'+eveui_urlify(dna)+'">'+(eveui_name||eveui_item_cache[ship_id].name)+'</a>]\n\t\t</span>\n\t\t<span class="eveui_icon eveui_icon" />\n\t\t<span class="eveui_icon eveui_copy_icon" />\n\t\t<span data-itemid="'+ship_id+'" class="eveui_icon eveui_info_icon" />\n\t\t',eveui_allow_edit&&(html+='\n\t\t\t<span class="eveui_icon" />\n\t\t\t<span class="eveui_icon" />\n\t\t\t<span class="eveui_icon eveui_more_icon" />\n\t\t\t'),html+="\n\t\t</div>\n\t\t<table>\n\t\t"+item_rows(high_slots,ship.hiSlots)+'\n\t\t<tr><td class="eveui_line_spacer">&nbsp;\n\t\t'+item_rows(med_slots,ship.medSlots)+'\n\t\t<tr><td class="eveui_line_spacer">&nbsp;\n\t\t'+item_rows(low_slots,ship.lowSlots)+'\n\t\t<tr><td class="eveui_line_spacer">&nbsp;\n\t\t'+item_rows(rig_slots,ship.rigSlots)+'\n\t\t<tr><td class="eveui_line_spacer">&nbsp;\n\t\t'+item_rows(subsystem_slots,ship.maxSubsystems)+'\n\t\t<tr><td class="eveui_line_spacer">&nbsp;\n\t\t'+item_rows(other_slots)+'\n\t\t</table>\n\t\t<span class="eveui_endcopy" />\n\t\t'}function eveui_fit_window(dna,eveui_name){eveui_mark("fit window created"),eveui_cache_fit(dna).done(function(){var eveui_window=$('.eveui_window[data-eveui-dna="'+dna+'"]');eveui_window.find(".eveui_content ").html(eveui_generate_fit(dna,eveui_name)),$(window).trigger("resize"),eveui_mark("fit window populated")})}function eveui_expand_fits(){var expand_filter="[data-eveui-expand]";"expand_all"==eveui_mode&&(expand_filter="*"),$(eveui_fit_selector).filter(expand_filter).each(function(){var dna=$(this).attr("data-dna")||this.href.substring(this.href.indexOf(":")+1),selected_element=$(this);eveui_cache_fit(dna).done(function(){var eveui_name=$(this).text().trim();selected_element.replaceWith('<span class="eveui_content">'+eveui_generate_fit(dna,eveui_name)+"</span>"),eveui_mark("fit window populated")})})}function eveui_lazy_preload(){var action_taken=!1;eveui_fit_preload>0&&$(eveui_fit_selector).each(function(i){var dna=$(this).data("dna")||this.href.substring(8);if(!eveui_fit_cache.hasOwnProperty(dna))return action_taken=!0,eveui_fit_preload--,eveui_cache_fit(dna).always(function(){clearTimeout(eveui_preload_timer),eveui_preload_timer=setTimeout(eveui_lazy_preload,eveui_preload_interval)}),!1}),action_taken||eveui_mark("preloading finished")}function eveui_cache_fit(dna){if("object"==typeof eveui_fit_cache[dna])return eveui_fit_cache[dna];var pending=[],items=dna.split(":");for(var item in items)if(0!=items[item].length){var match=items[item].split(";"),item_id=match[0];pending.push(eveui_cache_item(item_id))}return eveui_fit_cache[dna]=$.when.apply(null,pending).fail(function(){delete eveui_fit_cache[dna]}),eveui_fit_cache[dna]}function eveui_cache_item(item_id){return"object"==typeof eveui_item_cache[item_id]?"function"==typeof eveui_item_cache[item_id].promise?eveui_item_cache[item_id]:$.Deferred().resolve():eveui_item_cache[item_id]=$.ajax("https://crest-tq.eveonline.com/inventory/types/"+item_id+"/",{dataType:"json",cache:!0}).done(function(data){eveui_item_cache[item_id]=data}).fail(function(xhr){404==xhr.status||delete eveui_item_cache[item_id]})}function eveui_copy(element){$(".nocopy").hide(),$(".copyonly").show();var selection=window.getSelection(),range=document.createRange();element.find(".eveui_startcopy").length?(range.setStart(element.find(".eveui_startcopy")[0],0),range.setEnd(element.find(".eveui_endcopy")[0],0)):range.selectNodeContents(element[0]),selection.removeAllRanges(),selection.addRange(range),document.execCommand("copy"),selection.removeAllRanges(),$(".nocopy").show(),$(".copyonly").hide()}var eveui_preload_initial=50,eveui_preload_interval=10,eveui_mode="multi_window",eveui_allow_edit=!1,eveui_fit_selector="[href^=fitting],[data-dna]",eveui_item_selector="[href^=item],[data-itemid]",eveui_style="\n\t<style>\n\t\t.eveui_window {\n\t\t\tline-height: 1;\n\t\t\tbackground: #eee;\n\t\t\tborder: 1px solid;\n\t\t\topacity: 0.95;\n\t\t\tdisplay: flex;\n\t\t\tflex-direction: column;\n\t\t}\n\t\t.eveui_content td {\n\t\t\tpadding: 0 2px;\n\t\t}\n\t\t.eveui_modal_overlay {\n\t\t\tcursor: pointer;\n\t\t\tposition: fixed;\n\t\t\tbackground: #000;\n\t\t\ttop: 0;\n\t\t\tleft: 0;\n\t\t\tright: 0;\n\t\t\tbottom: 0;\n\t\t\tz-index: 10;\n\t\t\topacity: 0.5;\n\t\t}\n\t\t.eveui_title {\n\t\t\twidth: 100%;\n\t\t\tbackground: #ccc;\n\t\t\tcursor: move;\n\t\t\twhite-space: nowrap;\n\t\t\tmargin-right: 2em;\n\t\t}\n\t\t.eveui_scrollable {\n\t\t\tpadding-right: 17px;\n\t\t\ttext-align: left;\n\t\t\toverflow: auto;\n\t\t}\n\t\t.eveui_content {\n\t\t\twhite-space: nowrap;\n\t\t\tdisplay: inline-block;\n\t\t\tmargin: 2px;\n\t\t}\n\t\t.eveui_content div {\n\t\t\tdisplay: flex;\n\t\t}\n\t\t.eveui_flexgrow {\n\t\t\tflex-grow: 1;\n\t\t}\n\t\t.eveui_fit_header {\n\t\t\talign-items: center;\n\t\t}\n\t\t.eveui_line_spacer {\n\t\t\tline-height: 0.5em;\n\t\t}\n\t\t.eveui_numeric {\n\t\t\ttext-align: right;\n\t\t}\n\t\t.eveui_icon {\n\t\t\tdisplay: inline-block;\n\t\t\tmargin: 1px;\n\t\t\tvertical-align: middle;\n\t\t\theight: 1em;\n\t\t\twidth: 1em;\n\t\t\tbackground-position: center;\n\t\t\tbackground-repeat: no-repeat;\n\t\t\tbackground-size: contain;\n\t\t}\n\t\t.eveui_item_icon {\n\t\t\theight: 20px;\n\t\t\twidth: 20px;\n\t\t}\n\t\t.eveui_ship_icon {\n\t\t\theight: 32px;\n\t\t\twidth: 32px;\n\t\t}\n\t\t.eveui_close_icon {\n\t\t\tcursor: pointer;\n\t\t\tposition: absolute;\n\t\t\ttop: 0;\n\t\t\tright: 0;\n\t\t\tbackground-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxyZWN0IHg9IjciIHk9Ii0xIiB0cmFuc2Zvcm09Im1hdHJpeCgwLjcwNzEgLTAuNzA3MSAwLjcwNzEgMC43MDcxIC0zLjMxMzUgNy45OTk1KSIgd2lkdGg9IjIiIGhlaWdodD0iMTcuOTk5Ii8+CjxyZWN0IHg9IjciIHk9Ii0wLjk5OSIgdHJhbnNmb3JtPSJtYXRyaXgoLTAuNzA3MSAtMC43MDcxIDAuNzA3MSAtMC43MDcxIDcuOTk4OCAxOS4zMTQyKSIgd2lkdGg9IjIiIGhlaWdodD0iMTcuOTk5Ii8+PC9zdmc+Cg==);\n\t\t}\n\t\t.eveui_info_icon {\n\t\t\tcursor: pointer;\n\t\t\tbackground-image: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjEwMjQiIHdpZHRoPSI4OTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHBhdGggZD0iTTQ0OCAzODRjMzUgMCA2NC0yOSA2NC02NHMtMjktNjQtNjQtNjQtNjQgMjktNjQgNjQgMjkgNjQgNjQgNjR6IG0wLTMyMGMtMjQ3IDAtNDQ4IDIwMS00NDggNDQ4czIwMSA0NDggNDQ4IDQ0OCA0NDgtMjAxIDQ0OC00NDgtMjAxLTQ0OC00NDgtNDQ4eiBtMCA3NjhjLTE3NyAwLTMyMC0xNDMtMzIwLTMyMHMxNDMtMzIwIDMyMC0zMjAgMzIwIDE0MyAzMjAgMzIwLTE0MyAzMjAtMzIwIDMyMHogbTY0LTMyMGMwLTMyLTMyLTY0LTY0LTY0cy0zMiAwLTY0IDAtNjQgMzItNjQgNjRoNjRzMCAxNjAgMCAxOTIgMzIgNjQgNjQgNjQgMzIgMCA2NCAwIDY0LTMyIDY0LTY0aC02NHMwLTE2MCAwLTE5MnoiIC8+Cjwvc3ZnPgo=);\n\t\t}\n\t\t.eveui_plus_icon {\n\t\t\tcursor: pointer;\n\t\t\tbackground-image: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjEwMjQiIHdpZHRoPSI2NDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHBhdGggZD0iTTM4NCA0NDhWMTkySDI1NnYyNTZIMHYxMjhoMjU2djI1NmgxMjhWNTc2aDI1NlY0NDhIMzg0eiIgLz4KPC9zdmc+Cg==);\n\t\t}\n\t\t.eveui_minus_icon {\n\t\t\tcursor: pointer;\n\t\t\tbackground-image: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjEwMjQiIHdpZHRoPSI1MTIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHBhdGggZD0iTTAgNDQ4djEyOGg1MTJWNDQ4SDB6IiAvPgo8L3N2Zz4K);\n\t\t}\n\t\t.eveui_more_icon {\n\t\t\tcursor: pointer;\n\t\t\tbackground-image: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjEwMjQiIHdpZHRoPSI3NjgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHBhdGggZD0iTTAgNTc2aDEyOHYtMTI4aC0xMjh2MTI4eiBtMC0yNTZoMTI4di0xMjhoLTEyOHYxMjh6IG0wIDUxMmgxMjh2LTEyOGgtMTI4djEyOHogbTI1Ni0yNTZoNTEydi0xMjhoLTUxMnYxMjh6IG0wLTI1Nmg1MTJ2LTEyOGgtNTEydjEyOHogbTAgNTEyaDUxMnYtMTI4aC01MTJ2MTI4eiIgLz4KPC9zdmc+Cg==);\n\t\t}\n\t\t.eveui_edit_icon {\n\t\t\tcursor: pointer;\n\t\t\tbackground-image: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjEwMjQiIHdpZHRoPSI4OTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHBhdGggZD0iTTcwNCA2NEw1NzYgMTkybDE5MiAxOTIgMTI4LTEyOEw3MDQgNjR6TTAgNzY4bDAuNjg4IDE5Mi41NjJMMTkyIDk2MGw1MTItNTEyTDUxMiAyNTYgMCA3Njh6TTE5MiA4OTZINjRWNzY4aDY0djY0aDY0Vjg5NnoiIC8+Cjwvc3ZnPgo=);\n\t\t}\n\t\t.eveui_copy_icon {\n\t\t\tcursor: pointer;\n\t\t\tbackground-image: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjEwMjQiIHdpZHRoPSI4OTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHBhdGggZD0iTTcwNCA4OTZoLTY0MHYtNTc2aDY0MHYxOTJoNjR2LTMyMGMwLTM1LTI5LTY0LTY0LTY0aC0xOTJjMC03MS01Ny0xMjgtMTI4LTEyOHMtMTI4IDU3LTEyOCAxMjhoLTE5MmMtMzUgMC02NCAyOS02NCA2NHY3MDRjMCAzNSAyOSA2NCA2NCA2NGg2NDBjMzUgMCA2NC0yOSA2NC02NHYtMTI4aC02NHYxMjh6IG0tNTEyLTcwNGMyOSAwIDI5IDAgNjQgMHM2NC0yOSA2NC02NCAyOS02NCA2NC02NCA2NCAyOSA2NCA2NCAzMiA2NCA2NCA2NCAzMyAwIDY0IDAgNjQgMjkgNjQgNjRoLTUxMmMwLTM5IDI4LTY0IDY0LTY0eiBtLTY0IDUxMmgxMjh2LTY0aC0xMjh2NjR6IG00NDgtMTI4di0xMjhsLTI1NiAxOTIgMjU2IDE5MnYtMTI4aDMyMHYtMTI4aC0zMjB6IG0tNDQ4IDI1NmgxOTJ2LTY0aC0xOTJ2NjR6IG0zMjAtNDQ4aC0zMjB2NjRoMzIwdi02NHogbS0xOTIgMTI4aC0xMjh2NjRoMTI4di02NHoiIC8+Cjwvc3ZnPgo=);\n\t\t}\n\t\t.copy_only {\n\t\t\tposition: absolute;\n\t\t\tdisplay:inline-block;\n\t\t\tline-height: 0;\n\t\t\tfont-size: 0;\n\t\t}\n\t\t.nocopy::after {\n\t\t\tcontent: attr(data-content);\n\t\t}\n\t</style>\n\t",eveui_x=0,eveui_y=0,eveui_drag=null,eveui_drag_x=0,eveui_drag_y=0,eveui_zindex=100,eveui_preload_timer,eveui_fit_preload=eveui_preload_initial,eveui_fit_cache={},eveui_item_cache={};$(document).ready(function(){eveui_mark("document ready start"),$("head").append(eveui_style),$(document).on("click",".eveui_window .eveui_close_icon",function(e){$(this).parent().remove(),0==$(".eveui_window").length&&$(".eveui_modal_overlay").remove()}),$(document).on("click",".eveui_modal_overlay",function(e){$(".eveui_window").remove(),$(this).remove()}),$(document).on("click",eveui_fit_selector,function(e){if(e.preventDefault(),this.eveui_window&&document.contains(this.eveui_window[0]))return void this.eveui_window.remove();var dna=$(this).attr("data-dna")||this.href.substring(this.href.indexOf(":")+1),eveui_name=$(this).attr("data-title")||$(this).text().trim(),parent=$("body");switch(eveui_mode){case"modal":parent.append('<div class="eveui_modal_overlay" data-eveui-dna="'+dna+'" />');case"multi_window":this.eveui_window=eveui_new_window(),eveui_mark("fit window created"),this.eveui_window.attr("data-eveui-dna",dna),parent.append(this.eveui_window);break;case"expand":$(this).attr("data-eveui-expand",1),eveui_expand_fits()}eveui_fit_window(dna,eveui_name),$(window).trigger("resize")}),$(document).on("click",eveui_item_selector,function(e){if(e.preventDefault(),this.eveui_window&&document.contains(this.eveui_window[0]))return void this.eveui_window.remove();var item_id=$(this).attr("data-itemid")||this.href.substring(this.href.indexOf(":")+1);switch(this.eveui_window=eveui_new_window(),this.eveui_window.attr("data-eveui-itemid",item_id),eveui_mode){case"modal":$(this.closest(".eveui_window")).append(this.eveui_window);break;default:$("body").append(this.eveui_window)}eveui_mark("item window created"),eveui_cache_fit(item_id).done(function(){var eveui_window=$('.eveui_window[data-eveui-itemid="'+item_id+'"]'),html="";html+="<table>";var item=eveui_item_cache[item_id];for(var i in item.dogma.attributes){var attr=item.dogma.attributes[i];html+="<tr>",html+="<td>"+attr.attribute.name,html+="<td>"+attr.value}html+="</table>",eveui_window.find(".eveui_content").html(html),eveui_window.find(".eveui_title").html(item.name),$(window).trigger("resize"),eveui_mark("item window populated")}).fail(function(){var eveui_window=$('.eveui_window[data-eveui-itemid="'+item_id+'"]');eveui_window.remove()}),$(window).trigger("resize")}),$(document).on("click",".eveui_minus_icon",function(e){e.preventDefault();var item_id=$(this).closest("[data-eveui-itemid]").attr("data-eveui-itemid"),dna=$(this).closest("[data-eveui-dna]").attr("data-eveui-dna"),re=new RegExp(":"+item_id+";(\\d+)"),new_quantity=parseInt(dna.match(re)[1])-1;dna=new_quantity>0?dna.replace(re,":"+item_id+";"+new_quantity):dna.replace(re,""),$(this).closest("[data-eveui-dna]").attr("data-eveui-dna",dna),eveui_fit_window(dna)}),$(document).on("click",".eveui_plus_icon",function(e){e.preventDefault();var item_id=$(this).closest("[data-eveui-itemid]").attr("data-eveui-itemid"),dna=$(this).closest("[data-eveui-dna]").attr("data-eveui-dna"),re=new RegExp(":"+item_id+";(\\d+)"),new_quantity=parseInt(dna.match(re)[1])+1;dna=new_quantity>0?dna.replace(re,":"+item_id+";"+new_quantity):dna.replace(re,""),$(this).closest("[data-eveui-dna]").attr("data-eveui-dna",dna),eveui_fit_window(dna)}),$(document).on("click",".eveui_more_icon",function(e){e.preventDefault();var eveui_window=($(this).closest("[data-eveui-itemid]").attr("data-eveui-itemid"),$(this).closest("[data-eveui-dna]").attr("data-eveui-dna"),$('\n\t\t\t<span class="eveui_window" style="position:absolute">\n\t\t\t\t<span class="eveui_close_icon" />\n\t\t\t\t<span class="eveui_content">\n\t\t\t\t\tAutocomplete goes here\n\t\t\t\t</span>\n\t\t\t</span>\n\t\t\t'));eveui_window.css("z-index",eveui_zindex++),$(this).parent().after(eveui_window)}),$(document).on("click",".eveui_copy_icon",function(e){eveui_copy($(this).closest(".eveui_window"))}),$(document).on("mousedown",".eveui_window",function(e){$(this).css("z-index",eveui_zindex++)}),$(document).on("mousedown",".eveui_title",function(e){e.preventDefault(),eveui_drag=$(this).parent(),eveui_drag_x=eveui_x-eveui_drag.position().left,eveui_drag_y=eveui_y-eveui_drag.position().top,eveui_drag.css("z-index",eveui_zindex++)}),$(document).on("mousemove",function(e){eveui_x=e.clientX,eveui_y=e.clientY,null!==eveui_drag&&(eveui_drag.css("left",eveui_x-eveui_drag_x),eveui_drag.css("top",eveui_y-eveui_drag_y))}),$(document).on("mouseup",function(e){eveui_drag=null}),$(window).on("resize",function(e){if($(".eveui_window").each(function(){var eveui_window=$(this),eveui_content=eveui_window.find(".eveui_content");eveui_content.height()>window.innerHeight-20?eveui_window.css("height",window.innerHeight-20):eveui_window.css("height",""),eveui_content.width()>window.innerWidth-20?eveui_window.css("width",window.innerWidth-20):eveui_window.css("width",""),eveui_window[0].getBoundingClientRect().bottom>window.innerHeight&&eveui_window.css("top",window.innerHeight-eveui_window.height()-10),eveui_window[0].getBoundingClientRect().right>window.innerWidth&&eveui_window.css("left",window.innerWidth-eveui_window.width()-10)}),"modal"==eveui_mode){var eveui_window=$("body").children(".eveui_window");eveui_window.css("top",window.innerHeight/2-eveui_window.height()/2),eveui_window.css("left",window.innerWidth/2-eveui_window.width()/2)}}),eveui_preload_timer=setTimeout(eveui_lazy_preload,eveui_preload_interval),eveui_mark("document ready end"),eveui_expand_fits()}),String.prototype.repeat||(String.prototype.repeat=function(count){"use strict";if(null==this)throw new TypeError("can't convert "+this+" to object");var str=""+this;if(count=+count,count!=count&&(count=0),count<0)throw new RangeError("repeat count must be non-negative");if(count==1/0)throw new RangeError("repeat count must be less than infinity");if(count=Math.floor(count),0==str.length||0==count)return"";if(str.length*count>=1<<28)throw new RangeError("repeat count must not overflow maximum string size");for(var rpt="";1==(1&count)&&(rpt+=str),count>>>=1,0!=count;)str+=str;return rpt}),eveui_mark("script loaded");