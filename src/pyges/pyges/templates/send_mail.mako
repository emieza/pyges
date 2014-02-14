<html>
	<head>
		<title>Create Pages</title>
		<script type="text/javascript" src="static/wysiwyg/tinymce/tinymce.min.js" ></script>
		<script type="text/javascript">
			tinymce.init({
				selector : "textarea",
				theme : "modern",
				width : 900,
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
	<h1>Pyges: contact page</h1>

<form method="post">
	First name:<br>
	<input type="text" name="firstname" /><br>
	Second name:<br>
	<input type="text" name="surname" /><br>
	Email:<br>
	<input type="text" name="mail" /><br>
	Text:<br>
	<textarea name="text" rows="8" cols="80"></textarea><br>
	<input type="submit" value="Send">
</form>
% if missatge:
	${missatge} 
	
% endif
</body>
</html>
