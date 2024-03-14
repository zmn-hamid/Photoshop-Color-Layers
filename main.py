import photoshop.api as ps
import distinctipy

from config import FILE_NAME


# base
# FILE_NAME must be open before running this script
app = ps.Application()
doc = app.documents.getByName(FILE_NAME)

# setting ruler_units to pixels to avoid any problems
psPixels = 1
start_ruler_units = app.Preferences.RulerUnits
app.preferences.rulerUnits = ps.Units.Pixels

# in instance of SolidColor to be reused
chosenColor = ps.SolidColor()
# all the different colors possible
colors = list(distinctipy.get_colors(len(doc.layers)))

# main part
for idx, layer in enumerate(doc.layers):
    # select the layer
    doc.activeLayer = layer

    # select the visible pixels
    app.doJavaScript(
        """
        var id1268 = charIDToTypeID( "setd" );
        var desc307 = new ActionDescriptor();
        var id1269 = charIDToTypeID( "null" );
        var ref257 = new ActionReference();
        var id1270 = charIDToTypeID( "Chnl" );
        var id1271 = charIDToTypeID( "fsel" );
        ref257.putProperty( id1270, id1271 );
        desc307.putReference( id1269, ref257 );
        var id1272 = charIDToTypeID( "T   " );
        var ref258 = new ActionReference();
        var id1273 = charIDToTypeID( "Chnl" );
        var id1274 = charIDToTypeID( "Chnl" );
        var id1275 = charIDToTypeID( "Trsp" );
        ref258.putEnumerated( id1273, id1274, id1275 );
        desc307.putReference( id1272, ref258 );
        executeAction( id1268, desc307, DialogModes.NO )"""
    )

    # set the color
    rgb = [int(item * 255) for item in colors[idx]]
    (
        chosenColor.rgb.red,
        chosenColor.rgb.green,
        chosenColor.rgb.blue,
    ) = rgb

    # fill with color
    doc.selection.fill(chosenColor)

# setting the units back to what it was before
app.preferences.rulerUnits = start_ruler_units
