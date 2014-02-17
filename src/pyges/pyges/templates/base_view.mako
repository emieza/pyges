<html>
    <body>
        <div class="header">
            <%block name="header"/>
        </div>

        ${self.body()}

        <div class="footer">
            <%block name="footer">
                 Benvingut ${user}
            </%block>
        </div>
    </body>
</html>
