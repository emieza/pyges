<html>
	<head>
		<title>Create Pages</title>
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
	</head>
<body>
	<h1>Pyges: create page</h1>

	<form method="post">
        Language:
        <select name="lang">
        % for l in langs:
            <option value="${l}">${langs[l]}</option>
        % endfor
        </select>
        <br>
		Name:<br>
		<input type="text" name="title" /><br>
		Text:<br>
		<textarea name="text" rows="8" cols="80"></textarea><br>
		<input type="submit" value="Send">
	</form>
    <br>
    <a href="/">Return home</a>
</body>
</html>
