<html>
<head>
	<!-- WYSIWYG -->
	<script type="text/javascript" src="static/wysiwyg/tinymce/tinymce.min.js" ></script>
	<script type="text/javascript">
		tinymce.init({
			selector : "textarea",
			theme : "modern",
			width : 680,
			height : 300,
			plugins : ["advlist autolink link image lists charmap print preview hr anchor pagebreak", "searchreplace wordcount visualblocks visualchars insertdatetime media nonbreaking", "table contextmenu directionality emoticons paste textcolor responsivefilemanager filemanager"],
			toolbar1 : "undo redo | bold italic underline | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | styleselect",
			toolbar2 : "| responsivefilemanager | link unlink anchor | image media | forecolor backcolor  | print preview code ",
			image_advtab : true,
			relative_urls : false,
			external_filemanager_path : "static/wysiwyg/filemanager/",
			filemanager_title : "Responsive Filemanager",
		});
	</script>

	<!-- TRANSLATE -->
	<script type="text/javascript">
		window.onload = first_sel;
		function first_sel(){
			value = document.getElementById("sel_lang").value;
			var ajax = new XMLHttpRequest();
			ajax.open("GET","../../trans_view/" + value + "/${idsec}",false);
			ajax.send();
			document.getElementById("trans_view").innerHTML = ajax.responseText;
		}
		function select_option(sel){
			var ajax = new XMLHttpRequest();
			ajax.open("GET","../../trans_view/" + sel.options[sel.selectedIndex].value + "/${idsec}",false);
			ajax.send();
			document.getElementById("trans_view").innerHTML = ajax.responseText;
		}
	</script>

	<style type="text/css">
		.ct_tbl_cel { border: 1px solid black; padding: 5px; width:50%; vertical-align: top; } /* each cell */
		.ct_tbl_div { width: 100%; height: 100%; }
	</style>
</head>
<body>
	<h1>Pyges: create translation</h1>
	<h3>description</h3>
	<table>
		<tr>
			<td class="ct_tbl_cel">
				<br />
				<strong>Language: </strong>
				<select id="sel_lang" name="lang" onchange="select_option(this)">
				% for l in exl:
					<option value="${l}">${exl[l]}</option>
				% endfor
				</select>
				<br /><br />
				<div id="trans_view"></div>
				<br /><br />
			</td>
			<td class="ct_tbl_cel">
				% if len(exl) != 0:
					<form method="post">
						<input type="text" name="idsec" value="${idsec}" style="display:none;"/>
						<input type="text" name="lang" value="${ln}" style="display:none;" />
						<br />
						<strong>Language: </strong>
						${langs[ln]}
						<br /><br />
						<strong>Title: </strong>
						<input type="text" name="title" />
						<br /><br />
						<strong>Text: </strong>
						<br />
						<textarea name="text" rows="8" cols="80"></textarea>
						<br /><br />
						<input type="submit" value="Send">
					</form>
				% else:
					<div>All translations have been made</div>
				% endif
			</td>
		</tr>
	</table>
	<br />
	<a href="/trans_menu">Return menu translations</a>
	<br />
	<a href="/">Return home</a>

	<!--  -->
</body>
</html>
