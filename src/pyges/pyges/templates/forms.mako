
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Prova</title>
    <link rel="stylesheet" href="/deform_static/css/form.css"
          type="text/css"
            />
    <script type="text/javascript" src="/deform_static/scripts/jquery-1.4.2.min.js"></script>
    <script type="text/javascript" src="/deform_static/scripts/deform.js"></script>
    <script type="text/javascript" src="/deform_static/tinymce/jscripts/tiny_mce/tiny_mce.js"></script>
</head>
<body>
    <h2>Test de formularis</h2>
    ${form|n}
    
% if values:
    <b>Accepted page: ${values["title"]}</b>
    <br>
    <b>Body</b>:
    <br>
    <div id="body">${values["text"]|n}</body>
% endif

</body>
</html>
