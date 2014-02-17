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
	<style type="text/css">
		.et_tbl_cel { border: 1px solid black; padding: 5px; } /* each cell */
	</style>
</head>
<body>
	<h1>Pyges: edit translation</h1>
	<h3>description</h3>
	<table><tr><td class="et_tbl_cel">
		<form method="post">
			<input type="text" name="id" value="${id}" style="display:none;"/>
			<strong>Language: </strong>${langs[page.lang]}
			<br /><br />
			<strong>Title: </strong><input type="text" name="title" value="${page.title}"/>
			<br /><br />
			<strong>Text: </strong>
			<br />
			<textarea name="text" rows="8" cols="80">${page.text}</textarea>
			<br /><br />
			<input type="submit" value="Send">
		</form>
	</td></tr></table>
	<br />
	<a href="/trans_menu">Return menu translations</a>
	<br />
	<a href="/">Return home</a>

	<!--  -->
</body>
</html>
