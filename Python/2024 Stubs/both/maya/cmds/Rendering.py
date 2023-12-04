from typing import Union, Optional, List, Tuple, Any

def ambientLight(*args, ambientShade: Optional[Union[float, bool]] = ..., discRadius: Optional[Union[float, bool]] = ..., drs: Optional[Union[float, bool]] = ..., exclusive: bool = ..., exc: bool = ..., intensity: Optional[Union[float, bool]] = ..., i: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., pos: Optional[Union[Tuple[float, float, float], bool]] = ..., rgb: Optional[Union[Tuple[float, float, float], bool]] = ..., rotation: Optional[Union[Tuple[float, float, float], bool]] = ..., rot: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowColor: Optional[Union[Tuple[float, float, float], bool]] = ..., sc: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowDither: Optional[Union[float, bool]] = ..., sd: Optional[Union[float, bool]] = ..., shadowSamples: Optional[Union[int, bool]] = ..., sh: Optional[Union[int, bool]] = ..., softShadow: bool = ..., ss: bool = ..., useRayTraceShadows: bool = ..., rs: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    TlightCmd is the base class for other light commands.
    The ambientLight command is used to edit the parameters of
    existing ambientLights, or to create new ones. The default
    behaviour is to create a new ambientlight.
    
    This is the commmand that instantiates an ambientLight
    or edits the parameters of an existing one.
    TambientLightCmd inherits from TlightCmd which defines
    common flags like intensity, colour etc.
    See TlightCmd for a global picture of the light commands.
    Note that the flag fAmbientLightUsed indicates whether
    the command uses any ambient specific flags.
    That is, if a command doesn't use flags
    defined here, the boolean fAmbientLightUsed is set to
    false and thus the undo/redo information is not saved
    at this level.
    
    TambientLightCmd behaves like any other command, it
    has flags, saves undo information etc. the only slightly
    different behaviour is that it calls up to TlightCmd to
    complete the functionality of the command.
    Example	parseArgs:  TambientLightCmd defines
    ambientLight specific parameters like -ambientShade
    however, several other parameters are available in
    TlightCmd such as -intensity etc.  So when parsing
    the arguments, a call is made to TlightCmd::parseArgs
    to parse common parameters (like Intensity).

    Args:
        ambientShade | ambientShade: (create, edit, query) - ambientShade
        discRadius | drs: (create, edit, query) - radius of the disc around the light
        exclusive | exc: (create, query) - True if the light is exclusively assigned
        intensity | i: (create, query) - Intensity of the light
        name | n: (create, query) - Name of the light
        position | pos: (create, query) - Position of the light
        rgb | rgb: (create, query) - RGB colour of the light
        rotation | rot: (create, query) - Rotation of the light for orientation, where applicable
        shadowColor | sc: (create, query) - Color of the light's shadow
        shadowDither | sd: (create, edit, query) - dither the shadow
        shadowSamples | sh: (create, edit, query) - number of shadow samples.
        softShadow | ss: (create, edit, query) - soft shadow
        useRayTraceShadows | rs: (create, query) - True if ray trace shadows are to be used
    """
    ...


def assignViewportFactories(*args, materialFactory: Optional[Union[str, bool]] = ..., mf: Optional[Union[str, bool]] = ..., nodeType: Optional[Union[str, bool]] = ..., nt: Optional[Union[str, bool]] = ..., textureFactory: Optional[Union[str, bool]] = ..., tf: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Sets viewport factories for displays as materials or textures.

    Args:
        materialFactory | mf: (create, edit, query) - Set or query the materialFactory for the node type.
        nodeType | nt: (create, edit, query) - The node type.
        textureFactory | tf: (create, edit, query) - Set or query the textureFactory for the node type.
    """
    ...


def batchRender(*args, filename: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., melCommand: Optional[Union[str, bool]] = ..., mc: Optional[Union[str, bool]] = ..., numProcs: Optional[Union[int, bool]] = ..., n: Optional[Union[int, bool]] = ..., preRenderCommand: Optional[Union[str, bool]] = ..., prc: Optional[Union[str, bool]] = ..., remoteRenderMachine: Optional[Union[str, bool]] = ..., rm: Optional[Union[str, bool]] = ..., renderCommandOptions: Optional[Union[str, bool]] = ..., rco: Optional[Union[str, bool]] = ..., showImage: bool = ..., si: bool = ..., status: Optional[Union[str, bool]] = ..., st: Optional[Union[str, bool]] = ..., useRemoteRender: bool = ..., um: bool = ..., useStandalone: bool = ..., us: bool = ..., verbosity: Optional[Union[int, bool]] = ..., v: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    The batchRender command is used to spawn off a separate
    rendering session of the current maya file. If no
    mayaFile is specified, it'll ask you whether you want the
    current job killed. 
    
    The batchRender will spawn a separate maya process in which
    commands will be communicated to it through a commandPort. If Maya
    is unable to find an available port an error will be
    produced. Maya will attempt to use ports 7835 through 7844.

    Args:
        filename | f: (create) - Filename to be rendered; if empty, a temporary filename will be created.
        melCommand | mc: (create) - Mel command to execute to run a renderer other than the software renderer.
        numProcs | n: (create) - Number of processors to use (0 means use all available processors).
        preRenderCommand | prc: (create) - Command to be run prior to invoking a batch render.
        remoteRenderMachine | rm: (create) - Name of remote render machine. Not available on Windows.
        renderCommandOptions | rco: (create) - Arguments to the render command for batch rendering.
        showImage | si: (create) - Show progress of the current rendering job.
        status | st: (create) - Status string for displaying the batch render status.
        useRemoteRender | um: (create) - If remote rendering is desired. Not available on Windows.
        useStandalone | us: (create) - Batch rendering is to be done by exporting the scene and rendering with a standalone renderer.
        verbosity | v: (create) - Defines the verbosity level to report the batch rendering status: 1: display only one start message, then one message when all frames are rendered. 2: display only start and end frame messages. 3: display all messages (default).
    """
    ...


def binMembership(*args, addToBin: Optional[Union[str, bool]] = ..., add: Optional[Union[str, bool]] = ..., exists: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., inheritBinsFromNodes: Optional[Union[str, bool]] = ..., ibn: Optional[Union[str, bool]] = ..., isValidBinName: Optional[Union[str, bool]] = ..., ivn: Optional[Union[str, bool]] = ..., listBins: bool = ..., lb: bool = ..., makeExclusive: Optional[Union[str, bool]] = ..., mke: Optional[Union[str, bool]] = ..., notifyChanged: bool = ..., nfc: bool = ..., removeFromBin: Optional[Union[str, bool]] = ..., rm: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Command to assign nodes to bins.

    Args:
        addToBin | add: (create) - Add the nodes in a node list to a bin.
        exists | ex: (create) - Query if a node exists in a bin.  The exists flag can take only one node.
        inheritBinsFromNodes | ibn: (create) - Let the node in the flag's argument inherit bins from nodes in the specified node list.  The node list is specified as the object of the command.
        isValidBinName | ivn: (create) - Query if the specified bin name is valid.  If so, return true. Otherwise, return false.
        listBins | lb: (create, query) - Query and return a list of bins a list of nodes belong to. If a bin contains any of the nodes in the selection list, then it should be included in the returned bin list.
        makeExclusive | mke: (create) - Make the specified nodes belong exclusively in the specified bin.
        notifyChanged | nfc: (create) - This flag is used to notify that binMembership has been changed.
        removeFromBin | rm: (create) - Remove the nodes in a node list from a bin.
    """
    ...


def camera(*args, aspectRatio: Optional[Union[float, bool]] = ..., ar: Optional[Union[float, bool]] = ..., cameraScale: Optional[Union[float, bool]] = ..., cs: Optional[Union[float, bool]] = ..., centerOfInterest: Optional[Union[float, bool]] = ..., coi: Optional[Union[float, bool]] = ..., clippingPlanes: bool = ..., cp: bool = ..., depthOfField: bool = ..., dof: bool = ..., displayFieldChart: bool = ..., dfc: bool = ..., displayFilmGate: bool = ..., dfg: bool = ..., displayFilmOrigin: bool = ..., dfo: bool = ..., displayFilmPivot: bool = ..., dfp: bool = ..., displayGateMask: bool = ..., dgm: bool = ..., displayResolution: bool = ..., dr: bool = ..., displaySafeAction: bool = ..., dsa: bool = ..., displaySafeTitle: bool = ..., dst: bool = ..., fStop: Optional[Union[float, bool]] = ..., fs: Optional[Union[float, bool]] = ..., farClipPlane: Optional[Union[float, bool]] = ..., fcp: Optional[Union[float, bool]] = ..., farFocusDistance: Optional[Union[float, bool]] = ..., ffd: Optional[Union[float, bool]] = ..., filmFit: Optional[Union[str, bool]] = ..., ff: Optional[Union[str, bool]] = ..., filmFitOffset: Optional[Union[float, bool]] = ..., ffo: Optional[Union[float, bool]] = ..., filmRollOrder: Optional[Union[str, bool]] = ..., fro: Optional[Union[str, bool]] = ..., filmRollValue: Optional[Union[float, bool]] = ..., frv: Optional[Union[float, bool]] = ..., filmTranslateH: Optional[Union[float, bool]] = ..., fth: Optional[Union[float, bool]] = ..., filmTranslateV: Optional[Union[float, bool]] = ..., ftv: Optional[Union[float, bool]] = ..., focalLength: Optional[Union[float, bool]] = ..., fl: Optional[Union[float, bool]] = ..., focusDistance: Optional[Union[float, bool]] = ..., fd: Optional[Union[float, bool]] = ..., homeCommand: Optional[Union[str, bool]] = ..., hc: Optional[Union[str, bool]] = ..., horizontalFieldOfView: Optional[Union[float, bool]] = ..., hfv: Optional[Union[float, bool]] = ..., horizontalFilmAperture: Optional[Union[float, bool]] = ..., hfa: Optional[Union[float, bool]] = ..., horizontalFilmOffset: Optional[Union[float, bool]] = ..., hfo: Optional[Union[float, bool]] = ..., horizontalPan: Optional[Union[float, bool]] = ..., hpn: Optional[Union[float, bool]] = ..., horizontalRollPivot: Optional[Union[float, bool]] = ..., hrp: Optional[Union[float, bool]] = ..., horizontalShake: Optional[Union[float, bool]] = ..., hs: Optional[Union[float, bool]] = ..., journalCommand: bool = ..., jc: bool = ..., lensSqueezeRatio: Optional[Union[float, bool]] = ..., lsr: Optional[Union[float, bool]] = ..., lockTransform: bool = ..., lt: bool = ..., motionBlur: bool = ..., mb: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., nearClipPlane: Optional[Union[float, bool]] = ..., ncp: Optional[Union[float, bool]] = ..., nearFocusDistance: Optional[Union[float, bool]] = ..., nfd: Optional[Union[float, bool]] = ..., orthographic: bool = ..., o: bool = ..., orthographicWidth: Optional[Union[float, bool]] = ..., ow: Optional[Union[float, bool]] = ..., overscan: Optional[Union[float, bool]] = ..., ovr: Optional[Union[float, bool]] = ..., panZoomEnabled: bool = ..., pze: bool = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., p: Optional[Union[Tuple[float, float, float], bool]] = ..., postScale: Optional[Union[float, bool]] = ..., pts: Optional[Union[float, bool]] = ..., preScale: Optional[Union[float, bool]] = ..., prs: Optional[Union[float, bool]] = ..., renderPanZoom: bool = ..., rpz: bool = ..., rotation: Optional[Union[Tuple[float, float, float], bool]] = ..., rot: Optional[Union[Tuple[float, float, float], bool]] = ..., shakeEnabled: bool = ..., se: bool = ..., shakeOverscan: Optional[Union[float, bool]] = ..., so: Optional[Union[float, bool]] = ..., shakeOverscanEnabled: bool = ..., soe: bool = ..., shutterAngle: Optional[Union[float, bool]] = ..., sa: Optional[Union[float, bool]] = ..., startupCamera: bool = ..., sc: bool = ..., stereoHorizontalImageTranslate: Optional[Union[float, bool]] = ..., hit: Optional[Union[float, bool]] = ..., stereoHorizontalImageTranslateEnabled: bool = ..., she: bool = ..., verticalFieldOfView: Optional[Union[float, bool]] = ..., vfv: Optional[Union[float, bool]] = ..., verticalFilmAperture: Optional[Union[float, bool]] = ..., vfa: Optional[Union[float, bool]] = ..., verticalFilmOffset: Optional[Union[float, bool]] = ..., vfo: Optional[Union[float, bool]] = ..., verticalLock: bool = ..., vl: bool = ..., verticalPan: Optional[Union[float, bool]] = ..., vpn: Optional[Union[float, bool]] = ..., verticalRollPivot: Optional[Union[float, bool]] = ..., vrp: Optional[Union[float, bool]] = ..., verticalShake: Optional[Union[float, bool]] = ..., vs: Optional[Union[float, bool]] = ..., worldCenterOfInterest: Optional[Union[Tuple[float, float, float], bool]] = ..., wci: Optional[Union[Tuple[float, float, float], bool]] = ..., worldUp: Optional[Union[Tuple[float, float, float], bool]] = ..., wup: Optional[Union[Tuple[float, float, float], bool]] = ..., zoom: Optional[Union[float, bool]] = ..., zom: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create, edit, or query a camera with the specified properties. 
    
    The resulting camera can be repositioned using the viewPlace
    command. Many of the camera settings only affect the resulting
    rendered image. E.g. the F/Stop, shutter speed, the film related
    options, etc. Scaling the camera icon does not change any camera
    properties.

    Args:
        aspectRatio | ar: (create, edit, query) - The ratio of the film back width to the film back height.
        cameraScale | cs: (create, edit, query) - Scale the camera.
        centerOfInterest | coi: (create, edit, query) - Set the linear distance from the camera's eye point to the center of interest.
        clippingPlanes | cp: (create, edit, query) - Activate manual clipping planes.
        depthOfField | dof: (create, edit, query) - Determines whether a depth of field calculation is performed to give varying focus depending on the distance of the objects.
        displayFieldChart | dfc: (create, edit, query) - Activate display of the video field chart when looking through the camera.
        displayFilmGate | dfg: (create, edit, query) - Activate display of the film gate icons when looking through the camera.
        displayFilmOrigin | dfo: (create, edit, query) - Activate the display of the film origin guide when looking through the camera.
        displayFilmPivot | dfp: (create, edit, query) - Activate display of the film pivot guide when looking through the camera.
        displayGateMask | dgm: (create, edit, query) - Display the gate mask, file or resolution, as a shaded area to the edge of the viewport.
        displayResolution | dr: (create, edit, query) - Activate display of the current rendering resolution (as defined in the render globals) when looking through the camera.
        displaySafeAction | dsa: (create, edit, query) - Activate display of the video Safe Action guide when looking through the camera.
        displaySafeTitle | dst: (create, edit, query) - Activate display of the video Safe Title guide when looking through the camera.
        fStop | fs: (create, edit, query) - A real lens normally contains a diaphragm or other stop which blocks some of the light that would otherwise pass through it. This stop is usually approximately round, and its diameter as seen from the front of the lens is called the lens diameter. The lens diameter is often described by its relation to the focal length of the lens. A lens whose diameter is one-eighth its local length is said to have an F-stop of 8. This is an optical property of the lens.
        farClipPlane | fcp: (create, edit, query) - Specify the distance to the far clipping plane.
        farFocusDistance | ffd: (create, edit, query) - Linear distance to the far focus plane.
        filmFit | ff: (create, edit, query) - This describes how the digital image (in pixels) relates to the film back. Since the film back is defined in terms of real numbers with some arbitrary film aspect, and the digital image is defined in integer pixels with an equally arbitrary (and different) resolution, relating the two can get complicated. There are 4 choices:   horizontal  In this case the digital image is made to fit the film back exactly in the horizontal direction. This then gives each pixel a horizontal size = (film back width) / (horizontal resolution). The pixel height is then = (pixel width) / (pixel aspect ratio). Now that the pixel has a size, resolution gives us a complete image. That image will match the film back exactly in width. It will almost never match in height, either being too tall or too short. By playing with the numbers you can get it pretty close though. vertical This is the same idea as horizontal fit, only applied vertically. Thus the digital image will match the film back exactly in height, but miss in width. fill This is a convenience item. The system calculates both horizontal and vertical fits and then applies the one that makes the digital image larger than the film back. overscan Overscanning the film gate in the camera view allows us to choreograph action outside of the frustum from within the camera view without having to resort to a dolly or zoom. This feature is also essential for animating image planes.
        filmFitOffset | ffo: (create, edit, query) - Since we know from the above that the digital image may not match the film back exactly, we now have the question of how to position one relative to the other. Thus fit offset. Normally the centers are aligned. Fit offset lets you move the smaller image within the larger one. Specify the distance for film offset (inches).
        filmRollOrder | fro: (create, edit, query) - Specifies how the roll is applied with respect to the pivot value.  Rotate-Translate The film back is first rotated then translated by the pivot point value. Translate-Rotate The film back is first translated then rotated by the film roll value.
        filmRollValue | frv: (create, edit, query) - This specifies that amount of rotation around the film back. The roll value is specified in degrees. The rotation occurs around the specified pivot point. This value is used to compute a film roll matrix, which is a component of the post-projection matrix.
        filmTranslateH | fth: (create, edit, query) - The horizontal film translation. Values are normalized to the viewing area.
        filmTranslateV | ftv: (create, edit, query) - The vertical film translation. Values are normalized to the viewing area.
        focalLength | fl: (create, edit, query) - This is the distance along the lens axis between the lens and the film plane when "focal distance" is infinitely large. This is an optical property of the lens. This double precision parameter is always specified in millimeters.
        focusDistance | fd: (create, edit, query) - Set the focus at a certain distance in front of the camera.
        homeCommand | hc: (create, edit, query) - Specify the command to execute when "viewSet -home" is applied to this camera. All occurances of "%camera" will be replaced with the cameras name before viewSet runs the command.
        horizontalFieldOfView | hfv: (create, edit, query) - This is the film back width as seen by the lens when focused at infinity (ie., focal length away) measured as an angle. Note that it has nothing to do with pixels or the digital image or any aspects. Angle of view is a derived field, that is, it is not used internally by Alias and can be completely determined from other information. It is included as a convenience for the user. Its derivation is aov = 2 * atan( fbw / (2 * f) ) where "aov" is the angle of view, "fbw" is the film back width and "f" is the focal length.
        horizontalFilmAperture | hfa: (create, edit, query) - The horizontal width of the camera's film plane. The camera's film is located on the film plane. The extent of the film which will be exposed to an image of the scene in front of the lens is limited to a rectangular area described by the film back. This double precision parameter is always specified in inches.
        horizontalFilmOffset | hfo: (create, edit, query) - Horizontal offset from the center of the film back. Normally the film back will be centered on the lens axis. However, this need not be so. Film offset is the displacement of the center of the film back from the lens axis, also measured in inches. Note that offsetting the film back will distort the image, but will not alter the focus. This double precision parameter is always specified in inches.
        horizontalPan | hpn: (create, edit, query) - Horizontal 2D camera pan (inches)
        horizontalRollPivot | hrp: (create, edit, query) - The horizontal pivot point from the center of the film back. The pivot point is used during rotation of the film back.  The pivot is the point where the rotation occurs around. This double precision parameter corresponds to the normalized viewport. This value is a part of the post projection matrix.
        horizontalShake | hs: (create, edit, query) - Another horizontal offset from the center of the film back, which can be used and stored on the camera in addition to the horizonal film offset attribute.  This allows for film-based camera shake internal to the camera.  This works in exactly the same units and coordinates that the film offset attribute does. The effect of this attribute is toggled by the shake enabled attribute.
        journalCommand | jc: (create, edit, query) - Journal interactive camera commands. Commands can be undone when a camera is journaled.
        lensSqueezeRatio | lsr: (create, edit, query) - This is presently just an information field in the camera editor is meant to convey the horizontal distortion of the anamorphic lens normally used with some film formats. If it were used, it would do something like pixel aspect. Remember however that lens distortion (intentional or not) is slightly different than the output hardware's quantization. The fact that a "net" distortion parameter could be used for both may or may not confuse the issue.
        lockTransform | lt: (create, edit, query) - Lock the camera. When a camera is locked, its transformation information, that is, its Translate and Rotate properties cannot be adjusted, and the center of interest point cannot be moved. For orthographic cameras, Orthographic Width is also locked. For camera groups, Aim and Up locator's translate is also locked. For stereo cameras, the root camera is locked.
        motionBlur | mb: (create, edit, query) - Determines whether the camera's image is motion blured (as opposed to an object's image). For example, if you want to blur the camera movement when you are performing a flyby.
        name | n: (create, edit, query) - Name of the camera.
        nearClipPlane | ncp: (create, edit, query) - Specify the distance to the NEAR clipping plane.
        nearFocusDistance | nfd: (create, edit, query) - Linear distance to the near focus plane.
        orthographic | o: (create, edit, query) - Activate the orthographic camera.
        orthographicWidth | ow: (create, edit, query) - Set the orthographic projection width.
        overscan | ovr: (create, edit, query) - Set the percent of overscan.
        panZoomEnabled | pze: (create, edit, query) - Toggle camera 2D pan and zoom
        position | p: (create, edit, query) - Three linear values can be specified to translate the camera.
        postScale | pts: (create, edit, query) - The post-scale value.  This value multiplied against the computed projection matrix. It is applied after the the film roll.
        preScale | prs: (create, edit, query) - The pre-scale value. The value is multiplied against the computed projection matrix. It is applied before the film roll.
        renderPanZoom | rpz: (create, edit, query) - Toggle camera 2D pan and zoom in render
        rotation | rot: (create, edit, query) - Three angular values can be specified to rotate the camera.
        shakeEnabled | se: (create, edit, query) - Toggles the effect of the horizontal and vertical shake attributes.
        shakeOverscan | so: (create, edit, query) - Controls the amount of overscan in the output rendered image. For use when adding film-based camera shake.  Acts as a multiplier to the film aperture on the camera.
        shakeOverscanEnabled | soe: (create, edit, query) - Toggles the effect of the shake overscan attribute.
        shutterAngle | sa: (create, edit, query) - Specify the shutter angle (degrees).
        startupCamera | sc: (create, edit, query) - A startup camera is marked undeletable and implicit. This flag can be used to set or query the startup state of a camera. There must always be at least one startup camera.
        stereoHorizontalImageTranslate | hit: (create, edit, query) - A film-back offset for use in stereo camera rigs.
        stereoHorizontalImageTranslateEnabled | she: (create, edit, query) - Toggles the effect of the stereo HIT attribute.
        verticalFieldOfView | vfv: (create, edit, query) - Set the vertical field of view.
        verticalFilmAperture | vfa: (create, edit, query) - The vertical height of the camera's film plane. This double precision parameter is always specified in inches.
        verticalFilmOffset | vfo: (create, edit, query) - Vertical offset from the center of the film back. This double precision parameter is always specified in inches.
        verticalLock | vl: (create, edit, query) - Lock the size of the vertical film aperture.
        verticalPan | vpn: (create, edit, query) - Vertical 2D camera pan (inches)
        verticalRollPivot | vrp: (create, edit, query) - Vertical pivot point used for rotating the film back. This double precision parameter corresponds to the normalized viewport. This value is used to compute the film roll matrix, which is a component of the post projection matrix.
        verticalShake | vs: (create, edit, query) - Vertical offset from the center of the film back.  See horizontal shake attribute description.  This is toggled by the shake enabled attribute.
        worldCenterOfInterest | wci: (create, edit, query) - Camera world center of interest point.
        worldUp | wup: (create, edit, query) - Camera world up vector.
        zoom | zom: (create, edit, query) - The percent over the film viewable frustum to display
    """
    ...


def cameraSet(*args, active: bool = ..., a: bool = ..., appendTo: bool = ..., atl: bool = ..., camera: Optional[Union[str, bool]] = ..., cam: Optional[Union[str, bool]] = ..., clearDepth: bool = ..., cd: bool = ..., deleteAll: bool = ..., da: bool = ..., deleteLayer: bool = ..., d: bool = ..., insertAt: bool = ..., ins: bool = ..., layer: Optional[Union[int, bool]] = ..., l: Optional[Union[int, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., numLayers: bool = ..., nl: bool = ..., objectSet: Optional[Union[str, bool]] = ..., os: Optional[Union[str, bool]] = ..., order: Optional[Union[int, bool]] = ..., o: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command manages camera set nodes. Camera sets allow the users to
    break a single camera shot into layers. Instead of drawing all objects
    with a single camera, you can isolate the camera to only focus on
    certain objects and layer another camera into the viewport that draws
    the other objects. The situation to use camera sets primarily occurs
    when building stereoscopic scenes.
    
    For example, a set of stereo parameters may make the background
    objects divergent beyond the tolerable range of the human perceptual
    system. However, you like the settings because the main focus is in
    the foreground and the depth is important to the visual look of the
    scene.  You can use camera sets to break apart the shot into a
    foreground stereo camera and background stereo camera. The foreground
    stereo camera will retain the original parameters; however, it will
    only focus on the foreground elements.  The background stereo camera
    will have a different set of stereo parameters and will only draw the
    background element.
    
    Camera sets can be viewed using the stereo viewer and are currently only
    designed to work with stereo camera rigs.

    Args:
        active | a: (create, edit, query) - Gets / sets the active camera layer.
        appendTo | atl: (create, edit) - Append a new camera and/or object set to then end of the cameraSet layer list. This flag cannot be used in conjunction with insert flag. Additionally, it requires the camera and/or objectSet flag to be used.
        camera | cam: (create, edit, query) - Set/get the camera for a particular layer. When in query mode, You must specify the layer with the layer flag.
        clearDepth | cd: (create, edit, query) - Specifies if the drawing buffer should be cleared before beginning the draw for that layer.
        deleteAll | da: (create, edit) - Delete all camera layers
        deleteLayer | d: (create, edit) - Delete a layer from the camera set. You must specify the layer using the layer flag.
        insertAt | ins: (create, edit) - Inserts the specified camera and/or object set at the specified layer. This flag cannot be used in conjunction with the append flag. Additionally, this flag requires layer and camera (or objectSet) flag to be used.
        layer | l: (create, edit, query) - Specifies the layer index to be used when accessing layer information
        name | n: (create, query) - Gets or sets the name for the created camera set.
        numLayers | nl: (create, query) - Returns the number of layers defined in the specified cameraSet
        objectSet | os: (create, edit, query) - Set/get the objectSet for a particular layer. When in query mode, you must specify the layer with the layer flag.
        order | o: (create, edit, query) - Set the order in which a particular layer is processed. This flag must be used in conjunction with the layer flag.
    """
    ...


def cameraView(*args, addBookmark: bool = ..., ab: bool = ..., animate: bool = ..., an: bool = ..., bookmarkType: Optional[Union[int, bool]] = ..., typ: Optional[Union[int, bool]] = ..., camera: str = ..., c: str = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., removeBookmark: bool = ..., rb: bool = ..., setCamera: bool = ..., sc: bool = ..., setView: bool = ..., sv: bool = ..., edit: bool = ...) -> Any:
    r"""
    This command creates a preset view for a camera which is then
    independent of the camera. The view stores a camera's eye point,
    center of interest point, up vector, tumble pivot, horizontal
    aperture, vertical aperature, focal length, orthographic width,
    and whether the camera is orthographic or perspective by default.
    Or you can only store 2D pan/zoom attributes by setting the
    bookmarkType to 1. These settings can be applied to any other
    camera through the set camera flag. 
    
    This command can be used for creation or edit of camera view
    objects.  This command can only be executed with one of the add
    bookmark, or remove bookmark and one of set camera, or the set
    view flags set.

    Args:
        addBookmark | ab: (create, edit) - Associate this view with the camera specified or the camera in the active model panel. This flag can be used for creation or edit.
        animate | an: (create, edit) - Set the animation capability for view switches.
        bookmarkType | typ: (create) - Specify the bookmark type, which can be: 0. 3D bookmark; 1. 2D Pan/Zoom bookmark.
        camera | c: (edit) - Specify the camera to use. This flag should be used in conjunction with the add bookmark, remove bookmark, set camera, or set view flags. If this flag is not specified the camera in the active model panel will be used.
        name | n: (create) - Set the name of the view. This flag can only be used for creation.
        removeBookmark | rb: (edit) - Remove the association of this view with the camera specified or the camera in the active model panel. This can only be used with edit.
        setCamera | sc: (edit) - Set this view into a camera specified by the camera flag or the camera in the active model panel. This flag can only be used with edit.
        setView | sv: (edit) - Set the camera view to match a camera specified or the active model panel. This flag can only be used with edit.
    """
    ...


def checkDefaultRenderGlobals(*args, edit: bool = ..., query: bool = ...) -> Any:
    r"""
    To query whether or not the defaultRenderGlobals node has been modified since the last file save, use `ls -modified`. To force the scene to be dirty/clean use `file -modified`

    Args:
    """
    ...


def convertIffToPsd(*args, iffFileName: Optional[Union[str, bool]] = ..., ifn: Optional[Union[str, bool]] = ..., psdFileName: Optional[Union[str, bool]] = ..., pfn: Optional[Union[str, bool]] = ..., xResolution: Optional[Union[int, bool]] = ..., xr: Optional[Union[int, bool]] = ..., yResolution: Optional[Union[int, bool]] = ..., yr: Optional[Union[int, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Converts iff file to PSD file of given size

    Args:
        iffFileName | ifn: (create, query) - Input iff file name
        psdFileName | pfn: (create, query) - Output file name
        xResolution | xr: (create, query) - X resolution of the image
        yResolution | yr: (create, query) - Y resolution of the image
    """
    ...


def convertSolidTx(*args, alpha: bool = ..., al: bool = ..., antiAlias: bool = ..., aa: bool = ..., backgroundColor: Optional[Union[Tuple[int, int, int], bool]] = ..., bc: Optional[Union[Tuple[int, int, int], bool]] = ..., backgroundMode: Optional[Union[str, bool]] = ..., bm: Optional[Union[str, bool]] = ..., camera: Optional[Union[str, bool]] = ..., cam: Optional[Union[str, bool]] = ..., componentRange: bool = ..., cr: bool = ..., doubleSided: bool = ..., ds: bool = ..., fileFormat: Optional[Union[str, bool]] = ..., fil: Optional[Union[str, bool]] = ..., fileImageName: Optional[Union[str, bool]] = ..., fin: Optional[Union[str, bool]] = ..., fillTextureSeams: bool = ..., fts: bool = ..., force: bool = ..., f: bool = ..., fullUvRange: bool = ..., fur: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., pixelFormat: Optional[Union[str, bool]] = ..., pf: Optional[Union[str, bool]] = ..., resolutionX: Optional[Union[int, bool]] = ..., rx: Optional[Union[int, bool]] = ..., resolutionY: Optional[Union[int, bool]] = ..., ry: Optional[Union[int, bool]] = ..., reuseDepthMap: bool = ..., rdm: bool = ..., samplePlane: bool = ..., sp: bool = ..., samplePlaneRange: Optional[Union[Tuple[float, float, float, float], bool]] = ..., spr: Optional[Union[Tuple[float, float, float, float], bool]] = ..., shadows: bool = ..., sh: bool = ..., uvBBoxIntersect: bool = ..., ubi: bool = ..., uvRange: Optional[Union[Tuple[float, float, float, float], bool]] = ..., uvr: Optional[Union[Tuple[float, float, float, float], bool]] = ..., uvSetName: Optional[Union[str, bool]] = ..., uv: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to convert a texture on a surface to a file texture. The first
    argument is a rendering node or attribute. If only the node is
    specified, the outColor attribute will be sampled. If the node does
    not have an outColor attribute, the first attribute on the node which
    is: readable, not writable, not hidden, connectable, and not a multi
    is used. If lighting is to be baked, a shading group must be specified
    as the texture.
    
    The current selection will be used if a texture and surface are not
    specified.
    
    An image file will be generated for each object and stored in your
    image segment of your project. The filename will be formatted using
    the texture and surface names as follows:
    
     {texture}-{surface}.{fileExtension} 
    
    However, if force is off and there is a name collision a version
    number will be determined and the filename will be formatted as
    follows:
    
     {texture}-{surface}.{version}.{fileExtension} 
    
    If uv/uvsetName option is specified the filename will include
    {surface}-{uvname} instead of {surface}.

    Args:
        alpha | al: (create) - Specify whether to compute the transparency when baking lighting. The conversion will sample both the color and transparency of the shading network; the alpha channel of the file texture will be set to correspond to the result from sampling the transparency. By default transparency is not computed.
        antiAlias | aa: (create) - Perform anti-aliasing on the resulting image. Convert solid texture will generally take four times longer than without anti-aliasing. By default this flag is off.
        backgroundColor | bc: (create) - Set the background color to a specific value. Default is to use the shader default color to fill the background. Valid values range from 0 to 255 if the pixel format is 8 bits per channel, or 0 to 65535 if the pixel format is 16 bits per channel. This flag automatically sets -backgroundMode to "color". Default is black: 0 0 0.
        backgroundMode | bm: (create) - Defines how the background of the texture should be filled. Three modes are available: "shader" or 1: uses the default shader color. "color" or 2: uses the color given by -backgroundColor flag. "extend" or 3: extends outwards the color along the seam edges. Default is "shader".
        camera | cam: (create) - Specify a camera to use in baking lighting. If a camera is not specified the camera in the active view will be used.
        componentRange | cr: (create) - If one or more components have been selected to use, then if this flag is set, then the uv range of the components is used to fit into the texture map resolution. By default this flag is set to false.
        doubleSided | ds: (create) - Specify whether the sampler should flip the surface normal if the sample point faces away from the camera. Note: flipping the normal will make the result dependent on the camera (ie. one camera may flip normals where different camera wouldn't). It's not recommended that doubleSided be used in combination with shadows. By default this flag is false.
        fileFormat | fil: (create) - File format to be used for output. IFF is the default if unspecified. Other valid formats are: als: Alias PIX cin: Cineon eps: EPS gif: GIF iff: Maya IFF jpg: JPEG yuv: Quantel rla: Wavefront RLA sgi: SGI si: SoftImage (.pic) tga: Targa tif: TIFF bmp: Windows Bitmap
        fileImageName | fin: (create) - Specify the output path and name of file texture image. If the file name doesn't contain a directory separator, the image will be written to source images of the current project. The file will not be versioned if it already exists.
        fillTextureSeams | fts: (create) - Specify whether or not to overscan the polygon beyond its outer edges, when creating the file texture, in order to fill the texture seams. Default is true.
        force | f: (create) - If the output image already exists overwrite it. By default this flag is off.
        fullUvRange | fur: (create) - Sample using the full uv range of the surface. This flag cannot be used with the -uvr flag. A 2D texture placement node will be created and connected to the file texture. The placement's translate and coverage will be set according to the full UV range of the surface.
        name | n: (create) - Set the name of the file texture node. Name conflict resolution will be used to determine valid names when multiple objects are specified.
        pixelFormat | pf: (create) - Specifies the pixel format of the image. Note that not all file formats support all pixel formats. Available options: "8": 8 bits per channel, unsigned (0-255) "16": 16 bits per channel, unsigned (0-65535) Default is "8".
        resolutionX | rx: (create) - Set the horizontal image resolution. If this flag is not specified, the resolution will be set to 256.
        resolutionY | ry: (create) - Set the vertical image resolution. If this flag is not specified, the resolution will be set to 256.
        reuseDepthMap | rdm: (create) - Specify whether or not to reuse all the generated dmaps. Default is false.
        samplePlane | sp: (create) - Specify whether to sample using a virtual plane. This virtual plane has texture coordinates in the rectangle defined by the -samplePlaneRange flag. If the -samplePlaneRange flag is not set then the virtual plane defaults to having texture coordinates in the (0,0) to (1,1) square. If this option is set than all surface based arguments will be ignored.
        samplePlaneRange | spr: (create) - Specify the uv range of the texture coordinates used to sample if the -samplePlane option is set. There are four arguments corresponding to uMin, uMax, vMin and vMax. By default the virtual plane is from uMin 0 to uMax 1, and vMin 0 to vMax 1.
        shadows | sh: (create) - Specify whether to compute shadows when baking lighting. Disk based shadow maps will be used. Only lights with depth map shadows enabled will contribute to the shading. By default shadows are not computed.
        uvBBoxIntersect | ubi: (create) - This flag is obsolete.
        uvRange | uvr: (create) - Specify the uv range in which samples will be computed. There are four arguments corresponding to uMin, uMax, vMin and vMax. Each value should be specified based on the surface's uv space. A 2D texture placement node will be created and connected to the file texture. The placement's frame translate and coverage will be set according to the uv range specified. By default the entire uv range of the surface will be used.
        uvSetName | uv: (create) - Specify which uv set has to be used as the driving parametrization for convert solid.
    """
    ...


def convertTessellation(*args, allCameras: bool = ..., acm: bool = ..., camera: Optional[Union[str, bool]] = ..., cam: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Command to translate the basic tessellation attributes to advanced.
    If a camera flag is specified the translation will be based on the distance
    the surface is from the camera. The closer the surface is to the camera the
    more triangles there will be in the tessellation. If the "-allCameras" flags
    is specified, the renderable camera closest to the surface will be used to
    set the tessellation. The camera tessellation estimate is also dependent on
    the current render resolution; a higher resolution the result in a more
    finely tessellated surface.
    Multiple NURB surfaces may be specified on the command line, or if no
    command arguments are specified the surfaces on the active list will be
    used.
    This command operates by calculating the chord height such that smooth
    tessellation is achieved when the surface is rendered.  The advanced
    tessellation setting will be enabled on each surface specified, the
    primary tessellation parameters will be set, and chord height will be
    used as the secondary criteria.

    Args:
        allCameras | acm: (create) - Specifies that all renderable cameras should be used in calculating     the screen based tessellation.
        camera | cam: (create) - Specifies the camera which should be used in calculating the screen     based tessellation.
    """
    ...


def createLayeredPsdFile(*args, imageFileName: Optional[Union[Tuple[str, str, str], bool]] = ..., ifn: Optional[Union[Tuple[str, str, str], bool]] = ..., psdFileName: Optional[Union[str, bool]] = ..., psf: Optional[Union[str, bool]] = ..., xResolution: Optional[Union[int, bool]] = ..., xr: Optional[Union[int, bool]] = ..., yResolution: Optional[Union[int, bool]] = ..., yr: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    Creates a  layered PSD file with image names as input to individual layers

    Args:
        imageFileName | ifn: (create, multiuse) - Layer name, blend mode, Image file name  The image in the file will be transferred to layer specified. The image file specified can be in any of the formats supported by maya (ex. iff, jpg, gif, tif etc.). The blend mode options are : "Normal", "Dissolve", "Dark", "Multiply", "Color Burn", "Linear Burn", "Lighten", "Screen", "Color Dodge", "Linear Dogde", "Overlay", "Soft Light", "Hard Light", "Dissolve", "Vivid Light", "Linear Light", "Pin Light", "Hard Mix", "Difference", "Exclusion", "Hue", "Saturation", "Color",  "Luminosity"
        psdFileName | psf: (create) - PSD file name.
        xResolution | xr: (create) - X - resolution of the image.
        yResolution | yr: (create) - Y - resolution of the image.
    """
    ...


def createRenderLayer(*args, empty: bool = ..., e: bool = ..., g: bool = ..., makeCurrent: bool = ..., mc: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., noRecurse: bool = ..., nr: bool = ..., number: Optional[Union[int, bool]] = ..., num: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    Create a new render layer.  The render layer number will be assigned
    based on the first unassigned number not less than the base index number
    found in the render layer global parameters.  Normally all objects and
    their descendants will be added to the new render layer but if '-noRecurse'
    is specified then only the objects themselves will be added. Only transforms
    and geometry will be added to the new render layer.

    Args:
        empty | e: (create) - If set then create an empty render layer. The global flag or specified member list will take precidence over  use of this flag.
        g | g: (create) - If set then create a layer that contains all DAG objects in the scene. Any future objects created will also automatically become members of this layer. The global flag will take precidence over use of the empty flag or specified member list.
        makeCurrent | mc: (create) - If set then make the new render layer the current one.
        name | n: (create) - Name of the new render layer being created.
        noRecurse | nr: (create) - If set then only add specified objects to the render layer.  Otherwise all descendants will also be added.
        number | num: (create) - Number for the new render layer being created.
    """
    ...


def defaultLightListCheckBox(*args, annotation: Optional[Union[str, bool]] = ..., ann: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., bgc: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dgc: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., dpc: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., enableBackground: bool = ..., ebg: bool = ..., enableKeyboardFocus: bool = ..., ekf: bool = ..., exists: bool = ..., ex: bool = ..., fullPathName: bool = ..., fpn: bool = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., hlc: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., io: bool = ..., label: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., manage: bool = ..., m: bool = ..., noBackground: bool = ..., nbg: bool = ..., numberOfPopupMenus: bool = ..., npm: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., pma: bool = ..., preventOverride: bool = ..., po: bool = ..., shadingGroup: Optional[Union[str, bool]] = ..., sg: Optional[Union[str, bool]] = ..., statusBarMessage: Optional[Union[str, bool]] = ..., sbm: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., visible: bool = ..., vis: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., vcc: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a checkBox that controls whether a
    shadingGroup is connected/disconnected from the defaultLightList.

    Args:
        annotation | ann: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor | bgc: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag | dtg: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback | dgc: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback | dpc: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable | en: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground | ebg: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus | ekf: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName | fpn: (query) - Return the full path name of the widget, which includes all the parents.
        height | h: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor | hlc: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        isObscured | io: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        label | l: (create, edit) - Value of the checkbox label
        manage | m: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground | nbg: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfPopupMenus | npm: (query) - Return the number of popup menus attached to this control.
        parent | p: (create, query) - The parent layout for this control.
        popupMenuArray | pma: (query) - Return the names of all the popup menus attached to this control.
        preventOverride | po: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        shadingGroup | sg: (create, edit) - The shading group that is to be connected/disconnected from the defaultLightList.
        statusBarMessage | sbm: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        visible | vis: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand | vcc: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width | w: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def directionalLight(*args, decayRate: Optional[Union[int, bool]] = ..., d: Optional[Union[int, bool]] = ..., discRadius: Optional[Union[float, bool]] = ..., drs: Optional[Union[float, bool]] = ..., exclusive: bool = ..., exc: bool = ..., intensity: Optional[Union[float, bool]] = ..., i: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., pos: Optional[Union[Tuple[float, float, float], bool]] = ..., rgb: Optional[Union[Tuple[float, float, float], bool]] = ..., rotation: Optional[Union[Tuple[float, float, float], bool]] = ..., rot: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowColor: Optional[Union[Tuple[float, float, float], bool]] = ..., sc: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowDither: Optional[Union[float, bool]] = ..., sd: Optional[Union[float, bool]] = ..., shadowSamples: Optional[Union[int, bool]] = ..., sh: Optional[Union[int, bool]] = ..., softShadow: bool = ..., ss: bool = ..., useRayTraceShadows: bool = ..., rs: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    TlightCmd is the base class for other light commands.
    TnonAmbientLightCmd is a class that looks like a command but
    is not.  It is a base class for the extended/nonExtended
    lights.
    TnonExtendedLightCmd is a base class and not a real command. It is inherited by several
    lights: TpointLight, TdirectionalLight, TspotLight etc.
    The directionalLight command is used to edit the parameters
    of existing directionalLights, or to create new ones. The
    default behaviour is to create a new directionallight.
    
    This is the commmand that instantiates an directionalLight
    or edits the parameters of an existing one.
    TdirectionalLightCmd inherits from TnonExtendedLightCmd
    which defines softShadow flags.
    See TlightCmd for a global picture of the light commands.
    
    TdirectionalLightCmd behaves like any other command, it
    has flags, saves undo information etc. the only slightly
    different behaviour is that it calls up to
    TnonExtendedLightCmd to complete the functionality of
    the command.

    Args:
        decayRate | d: (create) - Decay rate of the light (0-no decay, 1-slow, 2-realistic, 3-fast)
        discRadius | drs: (create, query) - Radius of shadow disc.
        exclusive | exc: (create, query) - True if the light is exclusively assigned
        intensity | i: (create, query) - Intensity of the light
        name | n: (create, query) - Name of the light
        position | pos: (create, query) - Position of the light
        rgb | rgb: (create, query) - RGB colour of the light
        rotation | rot: (create, query) - Rotation of the light for orientation, where applicable
        shadowColor | sc: (create, query) - Color of the light's shadow
        shadowDither | sd: (create, query) - Shadow dithering value.
        shadowSamples | sh: (create, query) - Numbr of shadow samples to use
        softShadow | ss: (create, query) - True if soft shadowing is to be enabled
        useRayTraceShadows | rs: (create, query) - True if ray trace shadows are to be used
    """
    ...


def displacementToPoly(*args, findBboxOnly: bool = ..., fbb: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command bakes geometry with displacement mapping into a polygonal object.

    Args:
        findBboxOnly | fbb: (create, edit, query) - When used, only the bounding box scale for the displaced object is found.
    """
    ...


def doBlur(*args, colorFile: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., length: Optional[Union[float, bool]] = ..., l: Optional[Union[float, bool]] = ..., memCapSize: Optional[Union[float, bool]] = ..., o: Optional[Union[float, bool]] = ..., sharpness: Optional[Union[float, bool]] = ..., s: Optional[Union[float, bool]] = ..., smooth: Optional[Union[float, bool]] = ..., m: Optional[Union[float, bool]] = ..., smoothColor: bool = ..., r: bool = ..., vectorFile: Optional[Union[str, bool]] = ..., v: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    The doBlur command  will invoke the blur2d, which is a Maya
    stand-alone application to do 2.5 motion blur given the color image
    and the motion vector file.  For a given input colorFile name, e.g.
    "xxx.iff", the output blurred image will be "xxx_blur.iff" in the
    same directory as the input colorFile.  There is currently no control
    over the name of the output blurred image.

    Args:
        colorFile | c: (create) - Name of the input color image to be blurred.
        length | l: (create) - Scale applied on the motion vector. Ranges from 0 to infinity.
        memCapSize | o: (create) - Size of the memory cap, in bytes
        sharpness | s: (create) - Determines  the shape of the blur filter. The higher the value, the narrower the filter, the sharper the blur. The lower the value, the wider the filter, the more spread out the blur. Ranges from 0 to infinity.
        smooth | m: (create) - Filter size to smooth the blurred image. The higher the value, the more anti-aliased the alpha channel. Ranges from 1.0 to 5.0.
        smoothColor | r: (create) - Whether to smooth the color or not.
        vectorFile | v: (create) - Name of the input motion vector file.
    """
    ...


def dolly(*args, absolute: bool = ..., abs: bool = ..., distance: Optional[Union[float, bool]] = ..., d: Optional[Union[float, bool]] = ..., dollyTowardsCenter: bool = ..., dtc: bool = ..., orthoScale: Optional[Union[float, bool]] = ..., os: Optional[Union[float, bool]] = ..., relative: bool = ..., rel: bool = ...) -> Any:
    r"""
    The dolly command moves a camera along the viewing direction in
    the world space. The viewing-direction and up-direction of the
    camera are not altered. There are two modes of operation: 
    
    Relative mode: for a perspective camera, the camera is moved along
    its viewing direction, and the distance of travel is computed with
    respect to the current position of the camera in the world
    space. In relative mode, when the camera is moved, its COI is
    moved along with it, and is kept at the same distance, in front of
    the camera, as before applying the dolly operation. For
    orthographic camera, the viewing width of the camera is changed by
    scaling its ortho width by the new value specified on the command
    line. 
    
    Absolute mode: for a perspective camera, the camera is moved along
    its viewing direction, to the distance that is computed with
    respect to the current position of the world center of interest
    (COI) of the camera. In the absolute mode, when the camera is
    moved, the COI of the camera is not moved with the camera, but it
    is fixed at its current location in space. For orthographic
    camera, the viewing width of the camera is changed by replacing
    its ortho width with the new value specified on the command
    line. This command may be applied to more than one cameras;
    objects that are not cameras are ignored. When no camera name
    supplied on the command line, this command is applied to all
    currently active cameras. 
    
    The dolly command can be applied to either a perspective or an
    orthographic camera.

    Args:
        absolute | abs: (create) - This flag modifies the behavior of the distance and orthoScale flags. When used in conjunction with the distance flag, the distance argument specifies how far the camera's eye point should be set from the camera's center of interest. When used with the orthoScale flag, the orthoScale argument specifies the camera's new ortho width.
        distance | d: (create) - Unit distance to dolly a perspective camera.
        dollyTowardsCenter | dtc: (create) - This flag controls whether the dolly is performed towards the center of the view (if true), or towards the point where the user clicks (if false). By default, dollyTowardsCenter is on.
        orthoScale | os: (create) - Scale to change the ortho width of an orthographic camera.
        relative | rel: (create) - This flag modifies the behavior of the distance and orthoScale flags. When used in conjunction with the distance flag, the camera eye and center of interest are both moved by the amount specified by the distance flag's argument. When used with the orthoScale flag, the orthoScale argument is used multiply the camera's ortho width.By default the relative flag is always on.
    """
    ...


def editRenderLayerAdjustment(*args, attributeLog: bool = ..., alg: bool = ..., layer: Optional[Union[str, bool]] = ..., lyr: Optional[Union[str, bool]] = ..., nodeLog: bool = ..., nlg: bool = ..., remove: bool = ..., r: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create, edit, and query adjustments to render
    layers. An adjustment allows different attribute values or connections
    to be used depending on the active render layer.

    Args:
        attributeLog | alg: (query) - Output all adjustments for the specified layer sorted by attribute name.
        layer | lyr: (create, query) - Specified layer in which the adjustments will be modified. If not specified the active render layer will be used.
        nodeLog | nlg: (query) - Output all adjustments for the specified layer sorted by node name.
        remove | r: (create) - Remove the specified adjustments from the render layer. If an adjustment is removed from the current layer, the specified plug will revert back to it's master value determined by the default render layer.
    """
    ...


def editRenderLayerGlobals(*args, baseId: Optional[Union[int, bool]] = ..., bi: Optional[Union[int, bool]] = ..., currentRenderLayer: Optional[Union[str, bool]] = ..., crl: Optional[Union[str, bool]] = ..., enableAutoAdjustments: bool = ..., eaa: bool = ..., mergeType: Optional[Union[int, bool]] = ..., mt: Optional[Union[int, bool]] = ..., useCurrent: bool = ..., uc: bool = ..., query: bool = ...) -> Any:
    r"""
    Edit the parameter values common to all render layers.  Some of these
    paremeters, eg. baseId and mergeType, are stored as preferences and
    some, eg. currentRenderLayer, are stored in the file.

    Args:
        baseId | bi: (create, query) - Set base layer ID.  This is the number at which new layers start searching for a unique ID.
        currentRenderLayer | crl: (create, query) - Set current render layer. This will will update the renderLayerManger and all DAG objects to identify them as members of the render layer. This flag may also be used in conjunction with "useCurrent" to automatically add new DAG objects to the active layer. The "isCurrentRenderLayerChanging" condition can be used to determine when the current layer is being changed and adjustments are being applied to the scene.
        enableAutoAdjustments | eaa: (create, query) - Set whether or not to enable automatic creation of adjustments when certain attributes (ie. surface render stats, shading group assignment, or render settings) are changed.
        mergeType | mt: (create, query) - Set file import merge type.  Valid values are 0, none, 1, by number, and 2, by name.
        useCurrent | uc: (create, query) - Set whether or not to enable usage of the current render layer as the destination for all new nodes.
    """
    ...


def editRenderLayerMembers(*args, fullNames: bool = ..., fn: bool = ..., noRecurse: bool = ..., nr: bool = ..., remove: bool = ..., r: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to query and edit memberships to render layers. Only
    transform and geometry nodes may be members. At render time, all
    descendants of the members of a render layer will also be included in the
    render layer.

    Args:
        fullNames | fn: (query) - (Query only.) If set then return the full DAG paths of the objects in the layer.  Otherwise return just the name of the object.
        noRecurse | nr: (create) - If set then only add selected objects to the render layer.  Otherwise all descendants of the selected objects will also be added. This flag may be applied to adding or removing objects from the layer.
        remove | r: (create) - Remove the specified objects from the render layer.
    """
    ...


def exclusiveLightCheckBox(*args, annotation: Optional[Union[str, bool]] = ..., ann: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., bgc: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dgc: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., dpc: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., enableBackground: bool = ..., ebg: bool = ..., enableKeyboardFocus: bool = ..., ekf: bool = ..., exists: bool = ..., ex: bool = ..., fullPathName: bool = ..., fpn: bool = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., hlc: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., io: bool = ..., label: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., light: Optional[Union[str, bool]] = ..., lt: Optional[Union[str, bool]] = ..., manage: bool = ..., m: bool = ..., noBackground: bool = ..., nbg: bool = ..., numberOfPopupMenus: bool = ..., npm: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., pma: bool = ..., preventOverride: bool = ..., po: bool = ..., statusBarMessage: Optional[Union[str, bool]] = ..., sbm: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., visible: bool = ..., vis: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., vcc: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a checkBox that controls a light's exclusive
    non-exclusive status.  An exclusive light is one that is not
    hooked up to the default-light-list, thus it does not illuminate all
    objects be default.  However an exclusive light can be linked to
    an object.

    Args:
        annotation | ann: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor | bgc: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag | dtg: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback | dgc: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback | dpc: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable | en: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground | ebg: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus | ekf: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName | fpn: (query) - Return the full path name of the widget, which includes all the parents.
        height | h: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor | hlc: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        isObscured | io: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        label | l: (create, edit) - Value of the checkbox label
        light | lt: (create) - The light that is to be made exclusive/non-exclusive.
        manage | m: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground | nbg: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfPopupMenus | npm: (query) - Return the number of popup menus attached to this control.
        parent | p: (create, query) - The parent layout for this control.
        popupMenuArray | pma: (query) - Return the names of all the popup menus attached to this control.
        preventOverride | po: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        statusBarMessage | sbm: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        visible | vis: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand | vcc: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width | w: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def frameBufferName(*args, autoTruncate: bool = ..., a: bool = ..., camera: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., renderLayer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., renderPass: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Returns the frame buffer name for a given renderPass renderLayer and
    camera combination. Optionally, this command can apply a name truncation
    algorithm so that the frameBuffer name will respect the maximum length
    imposed by the destination file format, if applicable.

    Args:
        autoTruncate | a: (create) - use this flag to apply a name truncation algorithm so that the frameBuffer name will respect the maximum length imposed by the destination file format, if applicable.
        camera | c: (create) - Specify a camera
        renderLayer | l: (create) - Specify a renderer layer
        renderPass | p: (create) - Specify a renderer pass
    """
    ...


def getRenderDependencies(*args) -> Any:
    r"""
    Command to return dependencies of an image source.  Image sources (such
    as render targets) can depend on other upstream image sources that result
    from renderings of 3D scene, or renderings of 2D compositing graphs.
    This command returns these dependencies, so that they can be analyzed and
    rendered.

    Args:
    """
    ...


def getRenderTasks(*args, camera: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., renderLayer: Optional[Union[str, bool]] = ..., rl: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Command to return render tasks to render an image source.  Image
    source can depend on upstream image sources that result from
    renderings of 3D scene, or 2D renderings (e.g. render targets).
    This command obtains the graph of image source render dependencies,
    and creates render tasks according to these dependencies.  A render
    task has context, which can be camera, render layer, and resolution,
    or other, renderer-specific context.  Because of image source
    overrides, the render task context depends on the path through the
    render dependency graph, with the most upstream override for a context
    item applied.  As there can be multiple paths through a render
    dependency graph to a render dependency, there can be multiple render
    tasks for a given render dependency.

    Args:
        camera | c: (create) - Camera node to use in the render context for the image source render task.
        renderLayer | rl: (create) - Render layer to use in the render context for the image source render task.
    """
    ...


def glRender(*args, accumBufferPasses: Optional[Union[int, bool]] = ..., abp: Optional[Union[int, bool]] = ..., alphaSource: Optional[Union[str, bool]] = ..., antiAliasMethod: Optional[Union[str, bool]] = ..., aam: Optional[Union[str, bool]] = ..., cameraIcons: bool = ..., ci: bool = ..., clearClr: Optional[Union[Tuple[float, float, float], bool]] = ..., cc: Optional[Union[Tuple[float, float, float], bool]] = ..., collisionIcons: bool = ..., coi: bool = ..., crossingEffect: bool = ..., ce: bool = ..., currentFrame: bool = ..., cf: bool = ..., drawStyle: Optional[Union[str, bool]] = ..., ds: Optional[Union[str, bool]] = ..., edgeSmoothness: Optional[Union[float, bool]] = ..., es: Optional[Union[float, bool]] = ..., emitterIcons: bool = ..., ei: bool = ..., fieldIcons: bool = ..., fii: bool = ..., flipbookCallback: Optional[Union[str, bool]] = ..., fc: Optional[Union[str, bool]] = ..., frameEnd: Optional[Union[int, bool]] = ..., fe: Optional[Union[int, bool]] = ..., frameIncrement: Optional[Union[int, bool]] = ..., fi: Optional[Union[int, bool]] = ..., frameStart: Optional[Union[int, bool]] = ..., fs: Optional[Union[int, bool]] = ..., fullResolution: bool = ..., fr: bool = ..., grid: bool = ..., gr: bool = ..., imageDirectory: Optional[Union[str, bool]] = ..., id: Optional[Union[str, bool]] = ..., imageName: Optional[Union[str, bool]] = ..., imageSize: Optional[Union[Tuple[int, int, float], bool]] = ..., lightIcons: bool = ..., li: bool = ..., lightingMode: Optional[Union[str, bool]] = ..., lm: Optional[Union[str, bool]] = ..., lineSmoothing: bool = ..., ls: bool = ..., offScreen: bool = ..., os: bool = ..., renderFrame: Optional[Union[str, bool]] = ..., rf: Optional[Union[str, bool]] = ..., renderSequence: Optional[Union[str, bool]] = ..., rs: Optional[Union[str, bool]] = ..., sharpness: Optional[Union[float, bool]] = ..., sh: Optional[Union[float, bool]] = ..., shutterAngle: Optional[Union[float, bool]] = ..., sa: Optional[Union[float, bool]] = ..., textureDisplay: bool = ..., txd: bool = ..., transformIcons: bool = ..., ti: bool = ..., useAccumBuffer: bool = ..., uab: bool = ..., viewport: Optional[Union[Tuple[int, int, float], bool]] = ..., vp: Optional[Union[Tuple[int, int, float], bool]] = ..., writeDepthMap: bool = ..., wdm: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command provides access to the Hardware Render Manager (HRM). There
    is one-and-only-one HRM in maya. The HRM controls the rendering performed
    in the hardware render buffer window. This command allows shell scripts,
    to modify the render state, and to initiate a render request.

    Args:
        accumBufferPasses | abp: (edit, query) - Set the number of accum buffer render passes.
        alphaSource | alphaSource: (edit, query) - Control the alpha source when writing image files. Valid values include: off, alpha, red, green, blue, luminance, clamp, invClamp.
        antiAliasMethod | aam: (edit, query) - Set the method used for anti-aliasing polygons: off, uniform, gaussian.
        cameraIcons | ci: (edit, query) - Set display status of camera icons.
        clearClr | cc: (edit, query) - Set the viewport clear color (0 - 1).
        collisionIcons | coi: (edit, query) - Set display status of collison model icons.
        crossingEffect | ce: (edit, query) - Enable/disable image filtering with a convolution filter.
        currentFrame | cf: (query) - Returns the current frame being rendered.
        drawStyle | ds: (edit, query) - Set the object drawing style: boundingBox, points, wireframe, flatShaded, smoothShaded.
        edgeSmoothness | es: (edit, query) - Controls the amount of edge smoothing. A value of 0.0 gives no smoothing, 1.0 gives default smoothing, and any other value scales the amount of default smoothing. Must enable the accumulation buffer.
        emitterIcons | ei: (edit, query) - Set display status of emitter icons.
        fieldIcons | fii: (edit, query) - Set display status of field icons.
        flipbookCallback | fc: (edit, query) - Register a procedure to be called after the render sequence has completed. Used to build the flipbook pulldown menu. See the example section for more details about how to build this procedure.
        frameEnd | fe: (edit, query) - Set the last frame to be rendered.
        frameIncrement | fi: (edit, query) - Set the frame increment during rendering.
        frameStart | fs: (edit, query) - Set the first frame to be rendered.
        fullResolution | fr: (edit, query) - Enable/disable rendering to full image output resolution. Must set a valid image output resolution (-is).
        grid | gr: (edit, query) - Set display status of the grid.
        imageDirectory | id: (edit, query) - Set the directory for the image files.
        imageName | imageName: (edit, query) - Set the base name of the image files.
        imageSize | imageSize: (edit, query) - Set the image output size. Takes width, height and aspect ratio. Pass 0,0,0 to use current port size. The image size must be equal to or greater then the viewport size. Large images will be tiled if full resolution rendering has been enabled (-fr/fullResolution).
        lightIcons | li: (edit, query) - Set display status of light icons.
        lightingMode | lm: (edit, query) - Set the lighting mode used for rendering: all, selected, default.
        lineSmoothing | ls: (edit, query) - Enable/disable anti-aliased lines.
        offScreen | os: (edit, query) - When set, this toggle allow HRM to use an offscreen buffer to render the view. This allows HRM to work when the application is iconified, or obscured
        renderFrame | rf: (edit, query) - Render the current frame. Requires the name of the view in which to render.
        renderSequence | rs: (edit, query) - Render the current frame sequence. Requires the name of the view in which to render.
        sharpness | sh: (edit, query) - Control the sharpness level of the convolution filter.
        shutterAngle | sa: (edit, query) - Set the shutter angle used for motion blur (0 - 1). A value of 0.0 gives no blurring, 0.5 gives correct blurring, and 1.0 gives continuous blurring. Must enable the accumulation buffer.
        textureDisplay | txd: (edit, query) - Enable/disable texture map display.
        transformIcons | ti: (edit, query) - Set display status of transform icons.
        useAccumBuffer | uab: (edit, query) - Enable/disable the accumulation buffer.
        viewport | vp: (edit, query) - Set the viewport size. Pass in the width, height and aspect ratio. This size will be used for all test rendering and image output size unless full resolution (-fr) has been set and a valid image output size (-is) has been set.
        writeDepthMap | wdm: (edit, query) - Enable/disable writing of zdepth to image files.
    """
    ...


def glRenderEditor(*args, control: bool = ..., ctl: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., fmc: Optional[Union[str, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., hlc: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., lck: bool = ..., lookThru: Optional[Union[str, bool]] = ..., lt: Optional[Union[str, bool]] = ..., mainListConnection: Optional[Union[str, bool]] = ..., mlc: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., slc: Optional[Union[str, bool]] = ..., stateString: bool = ..., sts: bool = ..., unParent: bool = ..., up: bool = ..., unlockMainConnection: bool = ..., ulk: bool = ..., updateMainConnection: bool = ..., upd: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., viewCameraName: bool = ..., vcn: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a glRender view. This is a special view used for hardware
    rendering. This command is used to create and reparent the view
    as needed to support panels. See the glRender command for controlling
    the specific behavior of the hardware rendering.

    Args:
        control | ctl: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag | dtg: (create, edit, query) - Attaches a tag to the editor.
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter | f: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection | fmc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        highlightConnection | hlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        lockMainConnection | lck: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        lookThru | lt: (create, edit, query) - Specify which camera the glRender view should be using.
        mainListConnection | mlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        panel | pnl: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent | p: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        selectionConnection | slc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        stateString | sts: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        unParent | up: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection | ulk: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection | upd: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        viewCameraName | vcn: (query) - Returns the name of the current camera used by the glRenderPanel. This is a query only flag.
    """
    ...


def hwReflectionMap(*args, backTextureName: Optional[Union[str, bool]] = ..., bkn: Optional[Union[str, bool]] = ..., bottomTextureName: Optional[Union[str, bool]] = ..., bmn: Optional[Union[str, bool]] = ..., cubeMap: bool = ..., cm: bool = ..., decalMode: bool = ..., dm: bool = ..., enable: bool = ..., en: bool = ..., frontTextureName: Optional[Union[str, bool]] = ..., ftn: Optional[Union[str, bool]] = ..., leftTextureName: Optional[Union[str, bool]] = ..., ltn: Optional[Union[str, bool]] = ..., rightTextureName: Optional[Union[str, bool]] = ..., rtn: Optional[Union[str, bool]] = ..., sphereMapTextureName: Optional[Union[str, bool]] = ..., smn: Optional[Union[str, bool]] = ..., topTextureName: Optional[Union[str, bool]] = ..., tpn: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a hwReflectionMap node for having reflection on
    textured surfaces that currently have their boolean attribute
    displayHWEnvironment set to true.

    Args:
        backTextureName | bkn: (query) - This flag specifies the file texture name for the back side of the cube. Default is none When queried, this flag returns a string.
        bottomTextureName | bmn: (query) - This flag specifies the file texture name for the bottom side of the cube. Default is none When queried, this flag returns a string.
        cubeMap | cm: (query) - If on, the reflection of the textures is done using the cube mapping. Default is false. The reflection is done using sphere mapping. When queried, this flag returns a boolean.
        decalMode | dm: (query) - If on, the reflection color replaces the surface shading. Default is false. The reflection is multiplied to the surface shading. When queried, this flag returns a boolean.
        enable | en: (query) - If on, enable the corresponding hwReflectionMap node. Default is false. When queried, this flag returns a boolean.
        frontTextureName | ftn: (query) - This flag specifies the file texture name for the front side of the cube. Default is none When queried, this flag returns a string.
        leftTextureName | ltn: (query) - This flag specifies the file texture name for the left side of the cube. Default is none When queried, this flag returns a string.
        rightTextureName | rtn: (query) - This flag specifies the file texture name for the right side of the cube. Default is none When queried, this flag returns a string.
        sphereMapTextureName | smn: (query) - This flag specifies the file texture name for the sphere mapping option. Default is none When queried, this flag returns a string.
        topTextureName | tpn: (query) - This flag specifies the file texture name for the top side of the cube. Default is none When queried, this flag returns a string.
    """
    ...


def hwRender(*args, acceleratedMultiSampleSupport: bool = ..., ams: bool = ..., activeTextureCount: bool = ..., atc: bool = ..., camera: Optional[Union[str, bool]] = ..., cam: Optional[Union[str, bool]] = ..., currentFrame: bool = ..., cf: bool = ..., currentView: bool = ..., cv: bool = ..., edgeAntiAliasing: Optional[Union[Tuple[int, int], bool]] = ..., eaa: Optional[Union[Tuple[int, int], bool]] = ..., fixFileNameNumberPattern: bool = ..., fnp: bool = ..., frame: Optional[Union[float, bool]] = ..., f: Optional[Union[float, bool]] = ..., fullRenderSupport: bool = ..., frs: bool = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., imageFileName: bool = ..., ifn: bool = ..., layer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., limitedRenderSupport: bool = ..., lrs: bool = ..., lowQualityLighting: bool = ..., lql: bool = ..., noRenderView: bool = ..., nrv: bool = ..., notWriteToFile: bool = ..., nwf: bool = ..., printGeometry: bool = ..., pg: bool = ..., renderHardwareName: bool = ..., rhw: bool = ..., renderRegion: Optional[Union[Tuple[int, int, int, int], bool]] = ..., reg: Optional[Union[Tuple[int, int, int, int], bool]] = ..., renderSelected: bool = ..., rs: bool = ..., textureResolution: Optional[Union[int, bool]] = ..., res: Optional[Union[int, bool]] = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., writeAlpha: bool = ..., a: bool = ..., writeDepth: bool = ..., d: bool = ..., query: bool = ...) -> Any:
    r"""
    Renders an image or a sequence using the hardware rendering engine

    Args:
        acceleratedMultiSampleSupport | ams: (query) - This flag when used with query will return whether the graphics supports     hardware accelerated multi-sampling.
        activeTextureCount | atc: (query) - This flag when used with query will return the number of textures that     have been bound to the graphics by the hardware renderer.
        camera | cam: (create, query) - Specify the camera to use.  Use the first available camera if the camera         given is not found.
        currentFrame | cf: (create, query) - Render the current frame.
        currentView | cv: (create, query) - When turned on, only the current view will be rendered.
        edgeAntiAliasing | eaa: (create, query) - Enables multipass rendering. Controls for the number of exposures rendered per frame are provided in the form of two associated flag arguments. The first specifies the sampling algorithm:  0 - Uniform Weighted Grid Sampling 1 - Rotated Grid Super Sampling (RGSS) 2 - Gaussian Weighted Sampling   Use of a sampling method other than the others listed above, will result in use of the default sample method of Uniform Weighted Grid Sampling. The second argument specifies a number of samples to use. For each sampling algorithm there is a fixed set of sample counts available:  0 - Uniform Weighted Grid Sampling 1 Sample 3 Samples 4 Samples 5 Samples 7 Samples 9 Samples 16 Samples 25 Samples 36 Samples 1 - Rotated Grid Super Sampling (RGSS) 1 Sample 4 Samples 5 Samples 2 - Gaussian Weighted Sampling 1 Sample 3 Samples 4 Samples 5 Samples 7 Samples 9 Samples 16 Samples 25 Samples 36 Samples   Using a sampling count other than the allowable options for the given sampling method will result in using the default sample count of 5. The values passed via the command will override settings stored in the hardwareRenderGlobals node.
        fixFileNameNumberPattern | fnp: (create, query) - This flag allows the user to take the hardwareRenderGlobals     filename as the initial filename pattern,     fix the frame number pattern in the filename in a unique way,     returns the new filename pattern.  This does not change the     hardwareRenderGlobals's filename.
        frame | f: (create) - Specify the frame to render.
        fullRenderSupport | frs: (create, query) - This flag may be used in the create or query context.     In the create context, it will force the renderer to abort and not     render any frames if the hardware is not fully supported.         In the query context, it will return whether full quality rendering     is supported on the current graphics system. Please see the graphics     card qualification charts for an explanation of limited support.
        height | h: (create, query) - Height. If not used, the height is taken from the render globals settings.
        imageFileName | ifn: (create, query) - This flag let people query the image name for a specified frame.     The frame can be specified using the "-frame" flag.     When no "-frame" is used, the     current frame number is used.
        layer | l: (create, query) - Render the specified render layer.         Only this render layer will be rendered,         regardless of the renderable attribute value of the render layer.         The layer name will be appended to the output image file name.         The specified render layer becomes the current render layer before rendering,         and remains as current render layer after the rendering.
        limitedRenderSupport | lrs: (query) - This flag when used with query will return whether limited rendering is supported         on the current graphics system. Please see the graphics card qualification         charts for the current definition of limited support.
        lowQualityLighting | lql: (create, query) - Disable lighting evaluation per pixel (fragment).         Note: The values passed via the command will override settings stored in     the hardware render globals node.
        noRenderView | nrv: (create, query) - When turned on, the render view is not updated after image computation
        notWriteToFile | nwf: (create, query) - This flag is set to true if the user does not want to write     the image to a file.  It is set to false, otherwise.     The default value of the flag is "false".
        printGeometry | pg: (create, query) - Print the geomety objects as they get translated.
        renderHardwareName | rhw: (query) - This flag will create a graphics context and return the name of the     graphics hardware being used. The graphics hardware is determined by     creating an off screen buffer and querying the GL_RENDERER string     from OpenGL. If the off screen buffer cannot be created an empty     string is returned.
        renderRegion | reg: (create, query) - Render region. The parameters are 4 integers, indicating             left right bottom top     of the region.
        renderSelected | rs: (create, query) - Only renders the selected objects.
        textureResolution | res: (create, query) - Specify the desired resolution of baked textures.
        width | w: (create, query) - Width. If not used, the width is taken from the render globals settings.
        writeAlpha | a: (create, query) - Read the alpha channel of color buffer and return as tif file.
        writeDepth | d: (create, query) - Read the depth buffer and return as tif file.
    """
    ...


def hwRenderLoad(*args) -> Any:
    r"""
    Empty command used to force the dynamic load of HR render

    Args:
    """
    ...


def imagePlane(*args, camera: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., counter: bool = ..., cn: bool = ..., detach: bool = ..., d: bool = ..., dropFrame: bool = ..., df: bool = ..., fileName: Optional[Union[str, bool]] = ..., fn: Optional[Union[str, bool]] = ..., frameDuration: Optional[Union[int, bool]] = ..., fd: Optional[Union[int, bool]] = ..., height: Optional[Union[float, bool]] = ..., h: Optional[Union[float, bool]] = ..., imageSize: Optional[Union[Tuple[int, int], bool]] = ..., iz: Optional[Union[Tuple[int, int], bool]] = ..., lookThrough: Optional[Union[str, bool]] = ..., lt: Optional[Union[str, bool]] = ..., maintainRatio: bool = ..., mr: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., negTimesOK: bool = ..., nt: bool = ..., numFrames: Optional[Union[int, bool]] = ..., nf: Optional[Union[int, bool]] = ..., quickTime: bool = ..., qt: bool = ..., showInAllViews: bool = ..., sia: bool = ..., timeCode: Optional[Union[int, bool]] = ..., tc: Optional[Union[int, bool]] = ..., timeCodeTrack: bool = ..., tt: bool = ..., timeScale: Optional[Union[int, bool]] = ..., ts: Optional[Union[int, bool]] = ..., twentyFourHourMax: bool = ..., tf: bool = ..., width: Optional[Union[float, bool]] = ..., w: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The imagePlane command allows querying of various properties of
            an image plane and any movie in use by the image plane. It also supports
            creating and edit.
            The object passed to the command may either be an imagePlane node,
            or a camera, in which case the command uses the image plane attached
            to the camera (if any). If no object is passed in, the current
            selection is used.
            Currently, most movie related queries work only on 64 bit Windows systems.

    Args:
        camera | c: (create, edit, query) - When creating, it will try to attach the created image plane to the specified camera. If the given camera is invalid, creating will fail. When querying, it will query which camera current image plane is attaching to. If it has no camera attached to (free image plane), it will return an empty string. When edit, it will make the image plane attach to the new specified camera. If the camera given is invalid, it will do nothing. When the image plane is attached to a camera, the image plane's transform node will be set identity. The detach command will not restore the original position of the image plane. but the undo command will restore the original position of the image plane.
        counter | cn: () - Query the 'counter' flag of the movie's timecode format. If this is true, the timecode returned by the -timeCode flag will be a simple counter. If false, the returned timecode will be an array of integers (hours, minutes, seconds, frames).
        detach | d: (edit) - This flag can only be used in the edit mode, when this flag is used in edit, it will detach current image plane from any camera it attaches to and make it a free image plane.
        dropFrame | df: (query) - Query the 'drop frame' flag of the movie's timecode format.
        fileName | fn: (create, edit) - Set the image name for image plane to read.
        frameDuration | fd: (query) - Query the frame duration of the movie's timecode format.
        height | h: (create, edit, query) - Height of the image plane. When creating, if this flag is not specified, it will use 10.0 as default height.
        imageSize | iz: (query) - Get size of the loaded image.
        lookThrough | lt: (create, edit, query) - The camera currently used for image plane to look through.
        maintainRatio | mr: (create, edit, query) - Let the image plane respect the picture aspect ratio. When creating, if this flag is not specified, it will use true as default value.
        name | n: (create, query) - Set the image plane node name when creating or return the image plane name when querying.
        negTimesOK | nt: (query) - Query the 'neg times OK' flag of the movie's timecode format.
        numFrames | nf: (query) - Query the whole number of frames per second of the movie's timecode format.
        quickTime | qt: (query) - Query whether the image plane is using a QuickTime movie.
        showInAllViews | sia: (create, edit, query) - The flag is used to show the current image plane in all views or not.
        timeCode | tc: (query) - Query the whole number of frames per second of the movie's timecode format.
        timeCodeTrack | tt: (query) - Query whether the movie on the image plane has a timecode track.
        timeScale | ts: (query) - Query the timescale of the movie's timecode format.
        twentyFourHourMax | tf: (query) - Query the '24 hour max' flag of the movie's timecode format.
        width | w: (create, edit, query) - Width of the image plane. When creating, if this flag is not specified, it will use 10.0 as default width.
    """
    ...


def iprEngine(*args, copy: str = ..., cp: str = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., diagnostics: bool = ..., dig: bool = ..., estimatedMemory: bool = ..., mem: bool = ..., exists: bool = ..., ex: bool = ..., iprImage: Optional[Union[str, bool]] = ..., ipr: Optional[Union[str, bool]] = ..., motionVectorFile: bool = ..., mvf: bool = ..., object: Optional[Union[str, bool]] = ..., obj: Optional[Union[str, bool]] = ..., region: Optional[Union[Tuple[int, int, int, int], bool]] = ..., r: Optional[Union[Tuple[int, int, int, int], bool]] = ..., relatedFiles: bool = ..., rel: bool = ..., releaseIprImage: bool = ..., rii: bool = ..., resolution: bool = ..., res: bool = ..., scanlineIncrement: Optional[Union[str, bool]] = ..., sli: Optional[Union[str, bool]] = ..., showProgressBar: bool = ..., spb: bool = ..., startTuning: bool = ..., st: bool = ..., stopTuning: bool = ..., spt: bool = ..., underPixel: Tuple[int, int] = ..., un: Tuple[int, int] = ..., update: bool = ..., u: bool = ..., updateDepthOfField: bool = ..., udf: bool = ..., updateLightGlow: bool = ..., ulg: bool = ..., updateMotionBlur: bool = ..., umb: bool = ..., updatePort: Optional[Union[str, bool]] = ..., up: Optional[Union[str, bool]] = ..., updateShaderGlow: bool = ..., usg: bool = ..., updateShading: bool = ..., us: bool = ..., updateShadowMaps: bool = ..., usm: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to create or edit an iprEngine.  A iprEngine
    is an object that watches for changes to shading
    networks and automatically reshades to generate an
    up-to-date image.

    Args:
        copy | cp: (edit) - Copies the deep raster file, as well as its related files, to the new location.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        diagnostics | dig: (edit) - The diagnostics should be shown
        estimatedMemory | mem: (query) - Displays the estimated memory being used by IPR.
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        iprImage | ipr: (create, edit, query) - Specify the ipr image to use.
        motionVectorFile | mvf: (query) - Returns the name of the motion vector file used by IPR.
        object | obj: (create, edit, query) - The objects to be tuned.
        region | r: (create, edit, query) - The coordinates of the region to be tuned. The integers are in the sequence left bottom right top or x1,y2  x2,y2
        relatedFiles | rel: (query) - Returns the names for the related files, e.g, the non-glow-non-blur image, the motion vector file, and the depth-map files.
        releaseIprImage | rii: (edit) - The ipr image should be released and memory should    be freed.
        resolution | res: (query) - The width and height of the ipr file.
        scanlineIncrement | sli: (create, edit, query) - Set the scanline increment percentage.  If the height of the region being update is 240 pixels, and the scanlineIncrement is 10% then the image will refresh blocks of 24 scanlines.
        showProgressBar | spb: (create, edit, query) - Show progress bar during tuning.
        startTuning | st: (create, edit, query) - An ipr image has been specified and now changes to shading    networks should force an image to be produced.
        stopTuning | spt: (create, edit, query) - Tuning should cease but ipr image should not be closed.
        underPixel | un: (edit) - Get list of objects under the pixel sprcified.
        update | u: (create, edit) - Force an update.
        updateDepthOfField | udf: (create, edit) - Force a refresh of depth-of-field.
        updateLightGlow | ulg: (create, edit, query) - Automatically update when light glow changes.
        updateMotionBlur | umb: (create, edit, query) - Automatically update when 2.5D motion blur changes.
        updatePort | up: (create, edit, query) - The name of the port that is to be updated when pixel values are recomputed.  (not currently supported)
        updateShaderGlow | usg: (create, edit, query) - Automatically update when shader glow changes.
        updateShading | us: (create, edit, query) - Automatically update shading.
        updateShadowMaps | usm: (create, edit) - Force the shadow maps to be generated and an update to occur.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def layeredShaderPort(*args, annotation: Optional[Union[str, bool]] = ..., ann: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., bgc: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dgc: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., dpc: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., enableBackground: bool = ..., ebg: bool = ..., enableKeyboardFocus: bool = ..., ekf: bool = ..., exists: bool = ..., ex: bool = ..., fullPathName: bool = ..., fpn: bool = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., hlc: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., io: bool = ..., manage: bool = ..., m: bool = ..., noBackground: bool = ..., nbg: bool = ..., node: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., numberOfPopupMenus: bool = ..., npm: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., pma: bool = ..., preventOverride: bool = ..., po: bool = ..., selectedColorControl: Optional[Union[str, bool]] = ..., scc: Optional[Union[str, bool]] = ..., selectedTransparencyControl: Optional[Union[str, bool]] = ..., stc: Optional[Union[str, bool]] = ..., statusBarMessage: Optional[Union[str, bool]] = ..., sbm: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., visible: bool = ..., vis: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., vcc: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a 3dPort that displays an image representing
    the layered shader node specified.

    Args:
        annotation | ann: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor | bgc: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag | dtg: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback | dgc: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback | dpc: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable | en: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground | ebg: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus | ekf: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName | fpn: (query) - Return the full path name of the widget, which includes all the parents.
        height | h: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor | hlc: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        isObscured | io: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage | m: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground | nbg: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        node | n: (create) - Specifies the name of the newLayeredShader node this port will represent.
        numberOfPopupMenus | npm: (query) - Return the number of popup menus attached to this control.
        parent | p: (create, query) - The parent layout for this control.
        popupMenuArray | pma: (query) - Return the names of all the popup menus attached to this control.
        preventOverride | po: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        selectedColorControl | scc: (create) - Specifies the name of the UI-control that represents the currently selected layer's color.
        selectedTransparencyControl | stc: (create) - Specifies the name of the UI-control that represents the currently selected layer's transparency.
        statusBarMessage | sbm: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        visible | vis: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand | vcc: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width | w: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def layeredTexturePort(*args, annotation: Optional[Union[str, bool]] = ..., ann: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., bgc: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dgc: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., dpc: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., enableBackground: bool = ..., ebg: bool = ..., enableKeyboardFocus: bool = ..., ekf: bool = ..., exists: bool = ..., ex: bool = ..., fullPathName: bool = ..., fpn: bool = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., hlc: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., io: bool = ..., manage: bool = ..., m: bool = ..., noBackground: bool = ..., nbg: bool = ..., node: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., numberOfPopupMenus: bool = ..., npm: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., pma: bool = ..., preventOverride: bool = ..., po: bool = ..., selectedAlphaControl: Optional[Union[str, bool]] = ..., sac: Optional[Union[str, bool]] = ..., selectedBlendModeControl: Optional[Union[str, bool]] = ..., sbc: Optional[Union[str, bool]] = ..., selectedColorControl: Optional[Union[str, bool]] = ..., scc: Optional[Union[str, bool]] = ..., selectedIsVisibleControl: Optional[Union[str, bool]] = ..., svc: Optional[Union[str, bool]] = ..., statusBarMessage: Optional[Union[str, bool]] = ..., sbm: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., visible: bool = ..., vis: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., vcc: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a 3dPort that displays an image representing
    the layered texture node specified.

    Args:
        annotation | ann: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor | bgc: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag | dtg: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback | dgc: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback | dpc: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable | en: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground | ebg: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus | ekf: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName | fpn: (query) - Return the full path name of the widget, which includes all the parents.
        height | h: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor | hlc: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        isObscured | io: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage | m: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground | nbg: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        node | n: (create) - Specifies the name of the newLayeredTexture node this port will represent.
        numberOfPopupMenus | npm: (query) - Return the number of popup menus attached to this control.
        parent | p: (create, query) - The parent layout for this control.
        popupMenuArray | pma: (query) - Return the names of all the popup menus attached to this control.
        preventOverride | po: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        selectedAlphaControl | sac: (create) - Specifies the name of the UI-control that represents the currently selected layer's alpha.
        selectedBlendModeControl | sbc: (create) - Specifies the name of the UI-control that represents the currently selected layer's blend mode.
        selectedColorControl | scc: (create) - Specifies the name of the UI-control that represents the currently selected layer's color.
        selectedIsVisibleControl | svc: (create) - Specifies the name of the UI-control that represents the currently selected layer's visibility.
        statusBarMessage | sbm: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        visible | vis: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand | vcc: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width | w: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def lightlink(*args, b: bool = ..., hierarchy: bool = ..., h: bool = ..., light: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., make: bool = ..., m: bool = ..., object: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., sets: bool = ..., set: bool = ..., shadow: bool = ..., shd: bool = ..., shapes: bool = ..., shp: bool = ..., transforms: bool = ..., t: bool = ..., useActiveLights: bool = ..., ual: bool = ..., useActiveObjects: bool = ..., uao: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to make, break and query light linking
    relationships between lights/sets of lights and objects/sets of
    objects.
    
    If no make, break or query flag is specified and both lights and
    objects flags are present, the make flag is assumed to be specified.
    
    If no make, break or query flag is specified and only one of the
    lights and objects flags is present, the query flag is assumed to be
    specified.
    
    You can specify as many lights and objects as you like, using the
    multiuse -light and -object flags.
    
    A better way to perform light linking is to make sets of lights and
    sets of geometry. If you create a set which contains lights (such as
    the ceiling lights in your scene) and a set which contains geometry
    (such as the geometry of your character), you can then link the
    set containing lights with the set containing geometry
    in order to get those lights to illuminate those pieces of geometry.
    In addition, you can add and remove lights and geometry from their
    respective sets without having to make and break light links.

    Args:
        b | b: (create) - The presence of this flag on the command indicates that the command is being invoked to break links between lights and renderable objects.
        hierarchy | h: (create) - When querying, specifies whether the result should include the hierarchy of transforms above shapes linked to the queried light/object. The transforms considered part of the hierarchy do not include the transform immediately above the shape. Default is true.
        light | l: (create, multiuse) - The argument to the light flag specifies a node to be used by the command in performing the action as if the node is a light. This is a multiuse flag -- many light nodes can be specified in a single invocation of the lightlink command.
        make | m: (create) - The presence of this flag on the command indicates that the command is being invoked to make links between lights and renderable objects.
        object | o: (create, multiuse) - The argument to the object flag specifies a node to be used by the command in performing the action as if the node is an object. This is a multiuse flag -- many object nodes can be specified in a single invocation of the lightlink command.
        sets | set: (create) - When querying, specifies whether the result should include sets linked to the queried light/object. Default is true.
        shadow | shd: (create) - Specify that shadows are to be linked.
        shapes | shp: (create) - When querying, specifies whether the result should include shapes linked to the queried light/object. Default is true.
        transforms | t: (create) - When querying, specifies whether the result should include transforms immediately above shapes linked to the queried light/object. Default is true.
        useActiveLights | ual: (create) - Specify that active lights are to be used.
        useActiveObjects | uao: (create) - Specify that active objects are to be used.
    """
    ...


def lightList(*args, add: Optional[Union[str, bool]] = ..., remove: Optional[Union[str, bool]] = ..., rm: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Add/Remove a relationship between an object and the
    current light.
    Soon to be replaced by the connect-attribute command.

    Args:
        add | add: (create) - add object(s) to light list.
        remove | rm: (create) - remove object(s) to light list.
    """
    ...


def listCameras(*args, orthographic: bool = ..., o: bool = ..., perspective: bool = ..., p: bool = ...) -> Any:
    r"""
    Command to list all cameras. If no flags are given, both
    perspective and orthographic cameras will be displayed. This
    command returns an array of camera names. When the transform name
    uniquely identifies the camera it is used, otherwise the shape
    name will be returned.

    Args:
        orthographic | o: (create) - Display all orthographic cameras.
        perspective | p: (create) - Display all perspective cameras.
    """
    ...


def lookThru(*args, farClip: Optional[Union[float, bool]] = ..., fc: Optional[Union[float, bool]] = ..., nearClip: Optional[Union[float, bool]] = ..., nc: Optional[Union[float, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command sets a particular camera to look through in a view. This
    command may also be used to view the negative z axis of lights or
    other DAG objects. The standard camera tools can then be used to place
    the object.
    
    Note: if there are multiple objects under the transform selected,
    cameras and lights take precedence.

    Args:
        farClip | fc: (create) - Used when setting clip far plane for a new look thru camera. Will not affect the attributes of an existing camera. Clip values must come before shape or view.
        nearClip | nc: (create) - Used when setting near clip plane for a new look thru camera. Will not affect the attributes of an existing camera. Clip values must come before shape or view.
    """
    ...


def lsThroughFilter(*args, item: Optional[Union[str, bool]] = ..., it: Optional[Union[str, bool]] = ..., nodeArray: bool = ..., na: bool = ..., reverse: bool = ..., rv: bool = ..., selection: bool = ..., sl: bool = ..., sort: Optional[Union[str, bool]] = ..., so: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    List all objects in the world that pass a given filter.

    Args:
        item | it: (create, multiuse) - Run the filter on specified node(s), using the fast version of this command.
        nodeArray | na: (create) - Fast version that runs an entire array of nodes through the filter at one time.
        reverse | rv: (create) - Only available in conjunction with nodeArray flag. Reverses the order of nodes in the returned arrays if true.
        selection | sl: (create) - Run the filter on selected nodes only, using the fast version of this command.
        sort | so: (create) - Only available in conjunction with nodeArray flag. Orders the nodes in the returned array. Current options are: "byName", "byType", and "byTime".
    """
    ...


def makebot(*args, checkdepends: bool = ..., c: bool = ..., checkres: Optional[Union[int, bool]] = ..., r: Optional[Union[int, bool]] = ..., input: Optional[Union[str, bool]] = ..., i: Optional[Union[str, bool]] = ..., nooverwrite: bool = ..., nov: bool = ..., output: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., verbose: bool = ..., v: bool = ...) -> Any:
    r"""
    The makebot command takes an image file and produces a block
    ordered texture (BOT) file, to be used for texture caching.
    If a relative pathname is specified for the input image file,
    project management rules apply.  If a relative pathname is
    specified for the output BOT file, project management rules
    apply and gets put into the sourceImages directory.

    Args:
        checkdepends | c: (create) - the BOT file should only be generated if it doesn't already exists, or if it is older than the source file
        checkres | r: (create) - the BOT file should only be generated if its resolution (maximum of width and height) is larger than the minimum value specified by the argument
        input | i: (create) - input image file
        nooverwrite | nov: (create) - If -c and/or -r indicate that the BOT file should be generated but if already exists, then this flag will prevent the file from being overwritten
        output | o: (create) - output BOT file
        verbose | v: (create) - Makebot will provide feedback if this flag is specified
    """
    ...


def mayaHasRenderSetup(*args, enableCurrentSession: bool = ..., ecs: bool = ..., enableDuringTests: bool = ..., edt: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command controls and queries render setup states.

    Args:
        enableCurrentSession | ecs: (edit, query) - Enables or disables render setup for this Maya session only. This flag should only be called during Maya intialization. This flag is for internal use only, may change at any time and is unsupported.
        enableDuringTests | edt: (edit, query) - Switches render setup for this Maya session only, as legacy render layer mode is assumed during testing. This flag is for internal use only, may change at any time and is unsupported.
    """
    ...


def nodeIconButton(*args, align: Optional[Union[str, bool]] = ..., al: Optional[Union[str, bool]] = ..., annotation: Optional[Union[str, bool]] = ..., ann: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., bgc: Optional[Union[Tuple[float, float, float], bool]] = ..., command: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., disabledImage: Optional[Union[str, bool]] = ..., di: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dgc: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., dpc: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., enableBackground: bool = ..., ebg: bool = ..., enableKeyboardFocus: bool = ..., ekf: bool = ..., exists: bool = ..., ex: bool = ..., flipX: bool = ..., fx: bool = ..., flipY: bool = ..., fy: bool = ..., font: Optional[Union[str, bool]] = ..., fn: Optional[Union[str, bool]] = ..., fullPathName: bool = ..., fpn: bool = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., hlc: Optional[Union[Tuple[float, float, float], bool]] = ..., image: Optional[Union[str, bool]] = ..., i: Optional[Union[str, bool]] = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., imageOverlayLabel: Optional[Union[str, bool]] = ..., iol: Optional[Union[str, bool]] = ..., isObscured: bool = ..., io: bool = ..., label: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., labelOffset: Optional[Union[int, bool]] = ..., lo: Optional[Union[int, bool]] = ..., manage: bool = ..., m: bool = ..., marginHeight: Optional[Union[int, bool]] = ..., mh: Optional[Union[int, bool]] = ..., marginWidth: Optional[Union[int, bool]] = ..., mw: Optional[Union[int, bool]] = ..., noBackground: bool = ..., nbg: bool = ..., numberOfPopupMenus: bool = ..., npm: bool = ..., overlayLabelBackColor: Optional[Union[Tuple[float, float, float, float], bool]] = ..., olb: Optional[Union[Tuple[float, float, float, float], bool]] = ..., overlayLabelColor: Optional[Union[Tuple[float, float, float], bool]] = ..., olc: Optional[Union[Tuple[float, float, float], bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., pma: bool = ..., preventOverride: bool = ..., po: bool = ..., rotation: Optional[Union[float, bool]] = ..., rot: Optional[Union[float, bool]] = ..., statusBarMessage: Optional[Union[str, bool]] = ..., sbm: Optional[Union[str, bool]] = ..., style: Optional[Union[str, bool]] = ..., st: Optional[Union[str, bool]] = ..., useAlpha: bool = ..., ua: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., version: Optional[Union[str, bool]] = ..., ver: Optional[Union[str, bool]] = ..., visible: bool = ..., vis: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., vcc: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This control supports up to 3 icon images and 4 different display
    styles.  The icon image displayed is the one that best fits the
    current size of the control given its current style.
    
    This command creates a button that can be displayed with different
    icons, with or without a text label. If the button is drag and dropped
    onto other controls (e.g., HyperShade), the command will be executed and
    the return string will be used as the name of a dropped node.

    Args:
        align | al: (create, edit, query) - The label alignment.  Alignment values are "left", "right", and "center". By default, the label is aligned "center". Currently only available when -st/style is set to "iconAndTextCentered".
        annotation | ann: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor | bgc: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        command | c: (create, edit, query) - Command executed when the control is pressed. The command should return a string which will be used to facilitate node drag and drop.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        disabledImage | di: (create, edit, query) - Image used when the button is disabled. Image size must be the same as the image specified with the i/image flag. This is a Windows only flag.
        docTag | dtg: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback | dgc: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback | dpc: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable | en: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground | ebg: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus | ekf: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        flipX | fx: (create, edit, query) - Is the image flipped horizontally?
        flipY | fy: (create, edit, query) - Is the image flipped vertically?
        font | fn: (create, edit, query) - The font for the text.  Valid values are "boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont", "plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont", "smallObliqueLabelFont", "fixedWidthFont" and "smallFixedWidthFont".
        fullPathName | fpn: (query) - Return the full path name of the widget, which includes all the parents.
        height | h: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor | hlc: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        image | i: (create, edit, query) - If you are not providing images with different sizes then you may use this flag for the control's image. If the "iconOnly" style is set, the icon will be scaled to the size of the control.
        image1 | i1: (create, edit, query) - First of three possible icons. The icon that best fits the current size of the control will be displayed.
        image2 | i2: (create, edit, query) - Second of three possible icons. The icon that best fits the current size of the control will be displayed.
        image3 | i3: (create, edit, query) - Third of three possible icons. The icon that best fits the current size of the control will be displayed.
        imageOverlayLabel | iol: (create, edit, query) - A short string, up to 6 characters, representing a label that will be displayed on top of the image.
        isObscured | io: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        label | l: (create, edit, query) - The text that appears in the control.
        labelOffset | lo: (create, edit, query) - The label offset. Default is 0. Currently only available when -st/style is set to "iconAndTextCentered".
        manage | m: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        marginHeight | mh: (create, edit, query) - The number of pixels above and below the control content. The default value is 1 pixel.
        marginWidth | mw: (create, edit, query) - The number of pixels on either side of the control content. The default value is 1 pixel.
        noBackground | nbg: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfPopupMenus | npm: (query) - Return the number of popup menus attached to this control.
        overlayLabelBackColor | olb: (create, edit, query) - The RGBA color of the shadow behind the label defined by imageOverlayLabel. Default is 50% transparent black: 0 0 0 .5
        overlayLabelColor | olc: (create, edit, query) - The RGB color of the label defined by imageOverlayLabel. Default is a light grey: .8 .8 .8
        parent | p: (create, query) - The parent layout for this control.
        popupMenuArray | pma: (query) - Return the names of all the popup menus attached to this control.
        preventOverride | po: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        rotation | rot: (create, edit, query) - The rotation value of the image in radians.
        statusBarMessage | sbm: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        style | st: (create, edit, query) - The draw style of the control.  Valid styles are "iconOnly", "textOnly", "iconAndTextHorizontal", "iconAndTextVertical", and "iconAndTextCentered". (Note: "iconAndTextCentered" is only available on Windows). If the "iconOnly" style is set, the icon will be scaled to the size of the control.
        useAlpha | ua: (create, edit, query) - Is the image using alpha channel?
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        version | ver: (create, edit, query) - Specify the version that this control feature was introduced. The argument should be given as a string of the version number (e.g. "2013", "2014"). Currently only accepts major version numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").
        visible | vis: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand | vcc: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width | w: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def nodePreset(*args, attributes: Optional[Union[str, bool]] = ..., atr: Optional[Union[str, bool]] = ..., custom: Optional[Union[str, bool]] = ..., ctm: Optional[Union[str, bool]] = ..., delete: Optional[Union[Tuple[str, str], bool]] = ..., exists: Optional[Union[Tuple[str, str], bool]] = ..., ex: Optional[Union[Tuple[str, str], bool]] = ..., isValidName: Optional[Union[str, bool]] = ..., ivn: Optional[Union[str, bool]] = ..., list: Optional[Union[str, bool]] = ..., ls: Optional[Union[str, bool]] = ..., load: Optional[Union[Tuple[str, str], bool]] = ..., ld: Optional[Union[Tuple[str, str], bool]] = ..., save: Optional[Union[Tuple[str, str], bool]] = ..., sv: Optional[Union[Tuple[str, str], bool]] = ...) -> Any:
    r"""
    Command to save and load preset settings for a node.
    This command allows you to take a snapshot of the values of all attributes of a
    node and save it to disk as a preset with user specified name. Later the saved
    preset can be loaded and applied onto a different node of the same type. The
    end result is that the node to which the preset is applied takes on the same
    values as the node from which the preset was generated had at the time of the
    snapshot.

    Args:
        attributes | atr: (create) - A white space separated string of the named attributes to save to the preset file. If not specified, all attributes will be stored.
        custom | ctm: (create) - Specifies a MEL script for custom handling of node attributes that are not handled by the general save preset mechanism (ie. multis, dynamic attributes, or connections). The identifiers #presetName and #nodeName will be expanded before the script is run. The script must return an array of strings which will be saved to the preset file and issued as commands when the preset is applied to another node. The custom script can query #nodeName in determining what should be saved to the preset, or issue commands to query the selected node in deciding how the preset should be applied.
        delete | delete: (create) - Deletes the existing preset for the node specified by the first argument with the name specified by the second argument.
        exists | ex: (create) - Returns true if the node specified by the first argument already has a preset with a name specified by the second argument. This flag can be used to check if the user is about to overwrite an existing preset and thereby provide the user with an opportunity to choose a different name.
        isValidName | ivn: (create) - Returns true if the name consists entirely of valid characters for a preset name. Returns false if not. Because the preset name will become part of a file name and part of a MEL procedure name, some characters must be disallowed. Only alphanumeric characters and underscore are valid characters for the preset name.
        list | ls: (create) - Lists the names of all presets which can be loaded onto the specified node.
        load | ld: (create) - Sets the settings of the node specified by the first argument according to the preset specified by the second argument. Any attributes on the node which are the destinations of connections or whose children (multi children or compound children) are destinations of connections will not be changed by the preset.
        save | sv: (create) - Saves the current settings of the node specified by the first argument to a preset of the name specified by the second argument. If a preset for that node with that name already exists, it will be overwritten with no warning. You can use the -exists flag to check if the preset already exists. If an attribute of the node is the destination of a connection, the value of the attribute will not be written as part of the preset.
    """
    ...


def ogsRender(*args, activeMultisampleType: Optional[Union[str, bool]] = ..., mst: Optional[Union[str, bool]] = ..., activeRenderOverride: Optional[Union[str, bool]] = ..., cro: Optional[Union[str, bool]] = ..., activeRenderTargetFormat: Optional[Union[str, bool]] = ..., fpt: Optional[Union[str, bool]] = ..., availableFloatingPointTargetFormat: bool = ..., afp: bool = ..., availableMultisampleType: bool = ..., amt: bool = ..., availableRenderOverrides: bool = ..., aro: bool = ..., camera: Optional[Union[str, bool]] = ..., cam: Optional[Union[str, bool]] = ..., currentFrame: bool = ..., cf: bool = ..., currentView: bool = ..., cv: bool = ..., enableFloatingPointRenderTarget: bool = ..., efp: bool = ..., enableMultisample: bool = ..., ems: bool = ..., frame: Optional[Union[float, bool]] = ..., f: Optional[Union[float, bool]] = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., layer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., noRenderView: bool = ..., nrv: bool = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Renders an image or a sequence using the OGS rendering engine

    Args:
        activeMultisampleType | mst: (edit, query) - Query the current active multisample type.
        activeRenderOverride | cro: (edit, query) - Set or query the current active render override.
        activeRenderTargetFormat | fpt: (edit, query) - Query the current active floating point target format.
        availableFloatingPointTargetFormat | afp: (query) - Returns the names of available floating point render target format.
        availableMultisampleType | amt: (query) - Returns the names of available multisample type.
        availableRenderOverrides | aro: (query) - Returns the names of available render overrides.
        camera | cam: (create, edit, query) - Specify the camera to use.  Use the first available camera if the camera given is not found.
        currentFrame | cf: (create, edit, query) - Render the current frame.
        currentView | cv: (create, edit, query) - When turned on, only the current view will be rendered.
        enableFloatingPointRenderTarget | efp: (edit, query) - Enable/disable floating point render target.
        enableMultisample | ems: (edit, query) - Enable/disable multisample.
        frame | f: (create, edit) - Specify the frame to render.
        height | h: (create, edit, query) - The height flag pass the height to the ogsRender command. If not used, the height is taken from the render globals settings.
        layer | l: (create, edit, query) - Render the specified legacy render layer. Only this render layer will be rendered, regardless of the renderable attribute value of the render layer. The layer name will be appended to the output image file name. The specified render layer becomes the current render layer before rendering, and remains as current render layer after the rendering. This argument uses legacy render layers as this command does not recognize the newer renderSetup render layer system introduced in Maya 2016.
        noRenderView | nrv: (create, edit, query) - When turned on, the render view is not updated after image computation
        width | w: (create, edit, query) - The width flag pass the width to the ogsRender command. If not used, the width is taken from the render globals settings.
    """
    ...


def orbit(*args, horizontalAngle: Optional[Union[float, bool]] = ..., ha: Optional[Union[float, bool]] = ..., pivotPoint: Optional[Union[Tuple[float, float, float], bool]] = ..., pp: Optional[Union[Tuple[float, float, float], bool]] = ..., rotationAngles: Optional[Union[Tuple[float, float], bool]] = ..., ra: Optional[Union[Tuple[float, float], bool]] = ..., verticalAngle: Optional[Union[float, bool]] = ..., va: Optional[Union[float, bool]] = ...) -> Any:
    r"""
    The orbit command revolves the camera(s) horizontally and/or
    vertically in the perspective window. The rotation axis is with
    respect to the camera. 
    
    To revolve horizontally: the rotation axis is the camera up
    direction vector. To revolve vertically: the rotation axis is the
    camera left direction vector. 
    
    When both the horizontal and the vertical angles are supplied on
    the command line, the camera is firstly revolved horizontally,
    then revolved vertically. 
    
    This command may be applied to more than one camera; objects that
    are not cameras are ignored. When no camera name supplied, this command
    is applied to all currently active cameras.

    Args:
        horizontalAngle | ha: (create) - Angle to revolve horizontally.
        pivotPoint | pp: (create) - Used as the pivot point in the world space.
        rotationAngles | ra: (create) - Angle to revolve horizontally and vertically.
        verticalAngle | va: (create) - Angle to revolve vertically.
    """
    ...


def panZoom(*args, absolute: bool = ..., abs: bool = ..., downDistance: Optional[Union[float, bool]] = ..., d: Optional[Union[float, bool]] = ..., leftDistance: Optional[Union[float, bool]] = ..., l: Optional[Union[float, bool]] = ..., relative: bool = ..., rel: bool = ..., rightDistance: Optional[Union[float, bool]] = ..., r: Optional[Union[float, bool]] = ..., upDistance: Optional[Union[float, bool]] = ..., u: Optional[Union[float, bool]] = ..., zoomRatio: Optional[Union[float, bool]] = ..., z: Optional[Union[float, bool]] = ...) -> Any:
    r"""
    The panZoom command pans/zooms the 2D film.
    
    The panZoom command can be applied to either a perspective or an
    orthographic camera.
    
    When no camera name is supplied, this command is applied to the
    camera in the active view.

    Args:
        absolute | abs: (create) - This flag modifies the behavior of the distance and zoomRatio flags. If specified, the distance and zoomRatio value will be applied directly.
        downDistance | d: (create) - Set the amount of down pan distance in inches
        leftDistance | l: (create) - Set the amount of left pan distance in inches
        relative | rel: (create) - This flag modifies the behavior of the distance and zoomRatio flags. If specified, the distance or zoomRatio value is used multiply the camera's existing value. By default the relative flag is always on.
        rightDistance | r: (create) - Set the amount of right pan distance in inches
        upDistance | u: (create) - Set the amount of up pan distance in inches
        zoomRatio | z: (create) - Set the amount of zoom ratio
    """
    ...


def perCameraVisibility(*args, camera: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., exclusive: bool = ..., ex: bool = ..., hide: bool = ..., hi: bool = ..., remove: bool = ..., rm: bool = ..., removeAll: bool = ..., ra: bool = ..., removeCamera: bool = ..., rc: bool = ..., query: bool = ...) -> Any:
    r"""
    The perCameraVisibility command creates, queries and removes
    visibility relationships between DAG objects and cameras.
    These relationships are applied in any viewport that uses the cameras
    involved. (They are not used e.g. in rendering.)
    Objects can be set to be exclusive to a camera (meaning they will only
    be displayed in viewports using that camera; they will be hidden in other
    viewports) or hidden from a camera (meaning they will be not visible
    in any viewport using the camera).

    Args:
        camera | c: (create, query) - Specify the camera for the operation.
        exclusive | ex: (create, query) - Set objects as being exclusive to the given camera.
        hide | hi: (create, query) - Set objects as being hidden from the given camera.
        remove | rm: (create) - Used with exclusive or hide, removes the objects instead of adding them.
        removeAll | ra: (create) - Remove all exclusivity/hidden objects for all cameras.
        removeCamera | rc: (create) - Remove all exclusivity/hidden objects for the given camera.
    """
    ...


def pointLight(*args, decayRate: Optional[Union[int, bool]] = ..., d: Optional[Union[int, bool]] = ..., discRadius: Optional[Union[float, bool]] = ..., drs: Optional[Union[float, bool]] = ..., exclusive: bool = ..., exc: bool = ..., intensity: Optional[Union[float, bool]] = ..., i: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., pos: Optional[Union[Tuple[float, float, float], bool]] = ..., rgb: Optional[Union[Tuple[float, float, float], bool]] = ..., rotation: Optional[Union[Tuple[float, float, float], bool]] = ..., rot: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowColor: Optional[Union[Tuple[float, float, float], bool]] = ..., sc: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowDither: Optional[Union[float, bool]] = ..., sd: Optional[Union[float, bool]] = ..., shadowSamples: Optional[Union[int, bool]] = ..., sh: Optional[Union[int, bool]] = ..., softShadow: bool = ..., ss: bool = ..., useRayTraceShadows: bool = ..., rs: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The pointLight command is used to edit the parameters of
    existing pointLights, or to create new ones. The default
    behaviour is to create a new pointlight.

    Args:
        decayRate | d: (create, edit, query) - decay rate of the light (0-no decay, 1-slow, 2-realistic, 3-fast)
        discRadius | drs: (create, edit, query) - radius of the disc around the light
        exclusive | exc: (create, edit, query) - This flag is obsolete.
        intensity | i: (create, edit, query) - intensity of the light (expressed as a percentage)
        name | n: (create, edit, query) - specify the name of the light
        position | pos: (create, edit, query) - This flag is obsolete.
        rgb | rgb: (create, edit, query) - color of the light (0-1)
        rotation | rot: (create, edit, query) - This flag is obsolete.
        shadowColor | sc: (create, edit, query) - the shadow color
        shadowDither | sd: (create, edit, query) - dither the shadow
        shadowSamples | sh: (create, edit, query) - number of shadow samples.
        softShadow | ss: (create, edit, query) - soft shadow
        useRayTraceShadows | rs: (create, edit, query) - ray trace shadows
    """
    ...


def preferredRenderer(*args, fallback: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., makeCurrent: bool = ..., mc: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to set the preferred renderer. This command can be used
    to query the preferred renderer and to set the current renderer
    as the preferred one. It also allows users to specify a
    preferred fallback renderer.

    Args:
        fallback | f: (create, query) - Sets the preferred fallback renderer.
        makeCurrent | mc: (create) - Sets the current renderer as the preferred one.
    """
    ...


def prepareRender(*args, defaultTraversalSet: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., deregister: str = ..., d: str = ..., invokePostRender: bool = ..., ior: bool = ..., invokePostRenderFrame: bool = ..., iof: bool = ..., invokePostRenderLayer: bool = ..., iol: bool = ..., invokePreRender: bool = ..., irr: bool = ..., invokePreRenderFrame: bool = ..., irf: bool = ..., invokePreRenderLayer: bool = ..., irl: bool = ..., invokeSettingsUI: bool = ..., isu: bool = ..., label: Optional[Union[str, bool]] = ..., lbl: Optional[Union[str, bool]] = ..., listTraversalSets: bool = ..., lt: bool = ..., postRender: Optional[Union[str, bool]] = ..., por: Optional[Union[str, bool]] = ..., postRenderFrame: Optional[Union[str, bool]] = ..., pof: Optional[Union[str, bool]] = ..., postRenderLayer: Optional[Union[str, bool]] = ..., pol: Optional[Union[str, bool]] = ..., preRender: Optional[Union[str, bool]] = ..., prr: Optional[Union[str, bool]] = ..., preRenderFrame: Optional[Union[str, bool]] = ..., prf: Optional[Union[str, bool]] = ..., preRenderLayer: Optional[Union[str, bool]] = ..., prl: Optional[Union[str, bool]] = ..., restore: bool = ..., rtr: bool = ..., saveAssemblyConfig: bool = ..., sac: bool = ..., settingsUI: Optional[Union[str, bool]] = ..., sui: Optional[Union[str, bool]] = ..., setup: bool = ..., stp: bool = ..., traversalSet: Optional[Union[str, bool]] = ..., ts: Optional[Union[str, bool]] = ..., traversalSetInit: Optional[Union[str, bool]] = ..., tsi: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to register, manage and invoke render traversals.
    Render traversals are used to configure a scene to prepare it for rendering.
    This command has special support for scene assembly nodes.  To render scene
    assembly nodes, a rendering traversal can activate an appropriate
    representation, for each assembly node in the scene.  When rendering is
    done, this command can correspondingly restore the representation that was
    active before rendering on each assembly.
    Render traversals are grouped into traversal sets.  A render traversal set
    includes callbacks, or render traversals, for one or more of the following
    steps of rendering, ordered by decreasing level of granularity.
    A render traversal callback is an arbitrary script, either MEL or Python,
    that can transform the Maya scene for rendering purposes.
    
    preRender
    Traversal run once per render, before any rendering is performed.
    postRender
    Traversal run once per render, after all rendering has been performed.
    preRenderLayer
    Traversal run before rendering each render layer.
    postRenderLayer
    Traversal run after rendering each render layer.
    preRenderFrame
    Traversal run before rendering each frame.
    postRenderFrame
    Traversal run after rendering each frame.
    
    During a render view or batch render, Maya will run the render traversals from
    the same traversal set, the default traversal set.  Traversal sets are named,
    so multiple traversal sets can be registered with this command, and the
    default render traversal set can be switched to any one of these registered
    traversal sets.  When changing the default traversal set, the different
    render traversal callbacks (preRender, preRenderLayer, preRenderFrame,
    postRender, postRenderLayer, postRenderFrame) are switched as a unit.
    At render time, the software rendering code invokes the callbacks of the
    default traversal set.  The prepareRender scripting capability allows for the
    development of multiple rendering preparation scripts, including from plugins,
    to provide extensibility rather than being constrained to a single
    implementation.
    A special traversal set is the "null" traversal set.  It is the initial
    default traversal set, and cannot be deregistered.  It performs no work,
    and does not save and restore the assembly node active representation
    configuration.  It will provide WYSIWYG (What You See Is What You Get)
    rendering of assembly nodes, without switching to a different representation
    to render.
    Render traversals are invoked by Maya using this command's create mode.
    This is done by Maya's rendering infrastructure, and should not be required
    unless developing new render views or batch render code.  Most uses of this
    command will simply use the edit mode to register render traversals into a
    render traversal set, or the query mode to query the names of the render
    traversals in a render traversal set.
    Render Traversals versus Render MEL Scripts
    Render traversals are similar in intent to the user-specified pre- and
    post-render, pre- and post-render layer, pre- and post-render frame MEL
    script capability.  The difference with the user MEL scripts is
    that prepareRender is in addition to, and does not replace, the user
    MEL scripts, can register multiple render traversal sets and switch them,
    and supports both MEL and Python.  The MEL render scripts are run inside
    the scope of the render traversals, that is, the preRender traversal is
    run before the pre-render MEL script and the postRender traversal is run
    after the post-render MEL script, the preRenderLayer traversal is run before
    the pre-render layer MEL script and the postRenderLayer traversal is run
    after the post-render layer MEL script, and finally the preRenderFrame
    traversal is run before the pre-render frame MEL script and the
    postRenderFrame traversal is run after the post-render frame MEL script.
    Saving and Restoring State
    The prepareRender command has support for saving and restoring the active
    representation of assembly nodes in the scene.  Use the saveAssemblyConfig flag
    to indicate that the render traversal set requires saving the assembly node
    active representation before rendering begins, and should restore the
    assembly node active representation after rendering ends.
    It is the responsibility of render traversals that modify the scene in ways
    other than changing the active representation on assembly nodes to restore the
    scene to its previous state, most likely using the postRender, postRenderLayer,
    and postRenderFrame traversals.
    Note that Maya does not call the prepareRender -restore command on
    batch render completion, since batch rendering is done on a copy of the
    scene which is discarded once rendering terminates.  Implementors of
    render traversals may wish to check whether they are running in batch mode,
    to implement the same optimization.

    Args:
        defaultTraversalSet | dt: (edit, query) - Set or query the default traversal set.  The prepareRender command performs operations on the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        deregister | d: (edit) - Deregister a registered traversal set.  If the deregistered traversal set is the default traversal set, the new default traversal set will be the "null" traversal set.
        invokePostRender | ior: (create) - Invoke the postRender render traversal for a given traversal set.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        invokePostRenderFrame | iof: (create) - Invoke the postRenderFrame render traversal for a given traversal set.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        invokePostRenderLayer | iol: (create) - Invoke the postRenderLayer render traversal for a given traversal set.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        invokePreRender | irr: (create) - Invoke the preRender render traversal for a given traversal set.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        invokePreRenderFrame | irf: (create) - Invoke the preRenderFrame render traversal for a given traversal set.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        invokePreRenderLayer | irl: (create) - Invoke the preRenderLayer render traversal for a given traversal set.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        invokeSettingsUI | isu: (create) - Invoke the settings UI callback to populate a layout with UI controls, for a given traversal set.  The current UI parent will be a form layout, which the callback can query using the setParent command.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        label | lbl: (edit, query) - Set or query the label for a given traversal set.  The label is used for UI display purposes, and can be localized.  The traversal set will be the default, unless the -traversalSet flag is used to specify an explicit traversal set.
        listTraversalSets | lt: (query) - Query the supported render traversal sets.
        postRender | por: (edit, query) - Set or query the postRender render traversal for a given traversal set.  This traversal is run after a render.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        postRenderFrame | pof: (edit, query) - Set or query the postRenderFrame render traversal for a given traversal set.  This traversal is run after the render of a single frame, with a render layer.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        postRenderLayer | pol: (edit, query) - Set or query the postRenderLayer render traversal for a given traversal set.  This traversal is run after a render layer is rendered, within a render.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        preRender | prr: (edit, query) - Set or query the preRender render traversal for a given traversal set.  This traversal is run before a render.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        preRenderFrame | prf: (edit, query) - Set or query the preRenderFrame render traversal for a given traversal set.  This traversal is run before the render of a single frame, with a render layer.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        preRenderLayer | prl: (edit, query) - Set or query the preRenderLayer render traversal for a given traversal set.  This traversal is run before a render layer is rendered, within a render.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        restore | rtr: (create) - Clean up after rendering, including restoring the assembly active representation configuration for the whole scene, if the saveAssemblyConfig flag for the traversal set is true.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        saveAssemblyConfig | sac: (edit, query) - Set or query whether or not the assembly active representation configuration for the whole scene should be saved for a given traversal set.  The traversal set will be the default, unless the -traversalSet flag is used to specify an explicit traversal set.
        settingsUI | sui: (edit, query) - Set or query the settings UI callback for a given traversal set.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        setup | stp: (create) - Setup render preparation, including saving the assembly active representation configuration for the whole scene, if the saveAssemblyConfig flag for the traversal set is true.  Any previously-saved configuration will be overwritten.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        traversalSet | ts: (create, edit, query) - Set or query properties for the specified registered traversal set. 			In query mode, this flag needs a value.
        traversalSetInit | tsi: (edit, query) - Set or query the traversal set initialisation callback for a given traversal set. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set. This callback is invoked whenever the specified traversal set becomes the default. traversal set.
    """
    ...


def projectionManip(*args, fitBBox: bool = ..., fb: bool = ..., projType: Optional[Union[int, bool]] = ..., pt: Optional[Union[int, bool]] = ..., switchType: bool = ..., st: bool = ..., query: bool = ...) -> Any:
    r"""
    Various commands to set the manipulator to interesting positions.

    Args:
        fitBBox | fb: (create) - Fit the projection manipulator size and position to the shading group bounding box. The orientation is not modified.
        projType | pt: (create) - Set the projection type to the given value. Projection type values are:   1 = planar.  2 = spherical.  3 = cylindrical.  4 = ball.  5 = cubic.  6 = triplanar.  7 = concentric.  8 = camera.
        switchType | st: (create) - Loop over the allowed types. If the hardware shading is on, it loops over the hardware shadeable types (planar, cylindrical, spherical), otherwise, it loops over all the types. If there is no given value, it loops over the different projection types.
    """
    ...


def psdChannelOutliner(*args, addChild: Tuple[str, str] = ..., ach: Tuple[str, str] = ..., allItems: bool = ..., all: bool = ..., annotation: Optional[Union[str, bool]] = ..., ann: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., bgc: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., doubleClickCommand: Optional[Union[str, bool]] = ..., dcc: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dgc: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., dpc: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., enableBackground: bool = ..., ebg: bool = ..., enableKeyboardFocus: bool = ..., ekf: bool = ..., exists: bool = ..., ex: bool = ..., fullPathName: bool = ..., fpn: bool = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., hlc: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., io: bool = ..., manage: bool = ..., m: bool = ..., noBackground: bool = ..., nbg: bool = ..., numberOfItems: bool = ..., ni: bool = ..., numberOfPopupMenus: bool = ..., npm: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., pma: bool = ..., preventOverride: bool = ..., po: bool = ..., psdParent: str = ..., ppa: str = ..., removeAll: bool = ..., ra: bool = ..., removeChild: str = ..., rc: str = ..., select: str = ..., sel: str = ..., selectCommand: Optional[Union[str, bool]] = ..., sc: Optional[Union[str, bool]] = ..., selectItem: bool = ..., si: bool = ..., statusBarMessage: Optional[Union[str, bool]] = ..., sbm: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., visible: bool = ..., vis: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., vcc: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a psdChannelOutliner control which is capable of displaying
    a tree structure upto one level.

    Args:
        addChild | ach: (edit, multiuse) - This flag should be used along with the "-psdParent/ppa" flag. A string item gets added as a child to the parent specifed with "-psdParent/ppa" flag. The next string assigns an associated image name.
        allItems | all: (query) - Returns all the items in the form parent.child.
        annotation | ann: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor | bgc: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag | dtg: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        doubleClickCommand | dcc: (create, edit) - Specify the command to be executed when an item is double clicked.
        dragCallback | dgc: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback | dpc: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable | en: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground | ebg: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus | ekf: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName | fpn: (query) - Return the full path name of the widget, which includes all the parents.
        height | h: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor | hlc: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        isObscured | io: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage | m: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground | nbg: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfItems | ni: (query) - Total number of items in the control.
        numberOfPopupMenus | npm: (query) - Return the number of popup menus attached to this control.
        parent | p: (create, query) - The parent layout for this control.
        popupMenuArray | pma: (query) - Return the names of all the popup menus attached to this control.
        preventOverride | po: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        psdParent | ppa: (edit) - Adds an item string to the controls which is treated as parent.
        removeAll | ra: (edit) - Removes all the items from the control.
        removeChild | rc: (edit, multiuse) - Deletes the particular child of the parent as specifed in "-psdParent/ppa" flag.
        select | sel: (edit) - Select the named item.
        selectCommand | sc: (create, edit) - Specify the command to be executed when an item is selected.
        selectItem | si: (query) - Returns the selected items.
        statusBarMessage | sbm: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        visible | vis: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand | vcc: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width | w: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def psdEditTextureFile(*args, addChannel: Optional[Union[str, bool]] = ..., adc: Optional[Union[str, bool]] = ..., addChannelColor: Optional[Union[Tuple[str, float, float, float], bool]] = ..., acc: Optional[Union[Tuple[str, float, float, float], bool]] = ..., addChannelImage: Optional[Union[Tuple[str, str], bool]] = ..., aci: Optional[Union[Tuple[str, str], bool]] = ..., deleteChannel: Optional[Union[str, bool]] = ..., psdFileName: Optional[Union[str, bool]] = ..., psf: Optional[Union[str, bool]] = ..., snapShotImage: Optional[Union[str, bool]] = ..., ssi: Optional[Union[str, bool]] = ..., uvSnapPostionTop: bool = ..., uvt: bool = ...) -> Any:
    r"""
    Edits the existing PSD file. Addition and deletion of the channels (layer sets) are
    supported.

    Args:
        addChannel | adc: (create, multiuse) - Adds an empty layer set with the given name to a already existing PSD file.
        addChannelColor | acc: (create, multiuse) - (M) Specifies the filled color of  the layer which is created in a layer set given by the layer name.
        addChannelImage | aci: (create, multiuse) - (M) Specifies the image file name whose image needs to be added as a layer to a given layer set which is the first string.
        deleteChannel | deleteChannel: (create, multiuse) - (M) Deletes the channels (layer sets) from a PSD file. This is a multiuse flag.
        psdFileName | psf: (create) - PSD file name.
        snapShotImage | ssi: (create) - Image file name on the disk containing UV snapshot / reference image.
        uvSnapPostionTop | uvt: (create) - Specifies the position of UV snapshot image layer  in the PSD file. "True" positions this layer at the top and "False" positions the layer at the bottom next to the background layer in the PSD file
    """
    ...


def psdExport(*args, alphaChannelIdx: Optional[Union[int, bool]] = ..., aci: Optional[Union[int, bool]] = ..., bytesPerChannel: Optional[Union[int, bool]] = ..., bpc: Optional[Union[int, bool]] = ..., emptyLayerSet: bool = ..., els: bool = ..., format: Optional[Union[str, bool]] = ..., layerName: Optional[Union[str, bool]] = ..., lyn: Optional[Union[str, bool]] = ..., layerSetName: Optional[Union[str, bool]] = ..., lsn: Optional[Union[str, bool]] = ..., outFileName: Optional[Union[str, bool]] = ..., ofn: Optional[Union[str, bool]] = ..., preMultiplyAlpha: bool = ..., pma: bool = ..., psdFileName: Optional[Union[str, bool]] = ..., ifn: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Writes the Photoshop file layer set into different formats.  The output
            file depth (bit per channel ) can be different from that of the input.
            If the input is 16 bpc and output is 8 bpc, there will be data loss.

    Args:
        alphaChannelIdx | aci: (create, query) - Index of the alpha channel to output, if not supplied, writes out the default alpha channel.  The index is zero based. This is useful to write out specific alpha channels available as "Additional Alpha Channels" of Photoshop.
        bytesPerChannel | bpc: (create, query) - Output file depth. Any of these keyword:  0 for choosing depth based on input 1 for 8 bits per channel 2 for 16 bits per channel  Default is 0.
        emptyLayerSet | els: (create, query) - Option to check if the given layer set is empty or not.  This should be used in query mode and input file name and layer set names should be specified.
        format | format: (create, query) - Output file format. Any of these keyword: "iff", "sgi", "pic", "tif", "als", "gif", "rla", "jpg" Default is iff.
        layerName | lyn: (create, query) - Name of the layer to output.
        layerSetName | lsn: (create, query) - Name of the layer set to output, if not supplied, writes out the Composite image. 			In query mode, this flag needs a value.
        outFileName | ofn: (create, query) - Name(with path) of the output file.
        preMultiplyAlpha | pma: (create, query) - Option to multiply RGB colors with alpha values.  If (r,g,b,a) is the value of pixel, it will be changed to (r*a, g*a, b*a, a) when this flag is used.
        psdFileName | ifn: (create, query) - Name(with path) of the input Photoshop file. 			In query mode, this flag needs a value.
    """
    ...


def psdTextureFile(*args, channelRGB: Optional[Union[Tuple[str, int, int, int, int], bool]] = ..., chc: Optional[Union[Tuple[str, int, int, int, int], bool]] = ..., channels: Optional[Union[Tuple[str, int, bool], bool]] = ..., chs: Optional[Union[Tuple[str, int, bool], bool]] = ..., imageFileName: Optional[Union[Tuple[str, str, int], bool]] = ..., ifn: Optional[Union[Tuple[str, str, int], bool]] = ..., psdFileName: Optional[Union[str, bool]] = ..., psf: Optional[Union[str, bool]] = ..., snapShotImageName: Optional[Union[str, bool]] = ..., ssi: Optional[Union[str, bool]] = ..., uvSnapPostionTop: bool = ..., uvt: bool = ..., xResolution: Optional[Union[int, bool]] = ..., xr: Optional[Union[int, bool]] = ..., yResolution: Optional[Union[int, bool]] = ..., yr: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    Creates a Photoshop file with UVSnap shot image and the layer set
    names as the input.

    Args:
        channelRGB | chc: (create, multiuse) - (M) Layer set names, index, red, green and blue values are given as input. Using this flag, the layers created can be filled with specified colors.  This is a multi use flag.  The index specifies the placement order of layer sets in the created file.
        channels | chs: (create, multiuse) - (M) Layer set names and index are given as input. This is a multi use flag. A layer set with the given name will be created.  The second argument is the index which specifies the placement order of layer sets in the created file. The third argument is a boolean, if "true" a layer is created inside the layer set , "false" creates an  empty layer set
        imageFileName | ifn: (create, multiuse) - Image file name, Layerset name and index.  The image in the file will be transferred to layer set specified.  The index specifies the placement order of layer sets in the created psd file.  The image file specified can be in any of the formats supported by maya (ex. iff, jpg, gif, tif etc.)
        psdFileName | psf: (create) - PSD file name.
        snapShotImageName | ssi: (create) - Image file name on the disk containing UV snapshot / reference image.
        uvSnapPostionTop | uvt: (create) - Specifies the position of UV snapshot image layer  in the PSD file. "True" positions this layer at the top and "False" positions the layer at the bottom next to the background layer in the PSD file
        xResolution | xr: (create) - X - resolution of the image.
        yResolution | yr: (create) - Y - resolution of the image.
    """
    ...


def rampColorPort(*args, annotation: Optional[Union[str, bool]] = ..., ann: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., bgc: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dgc: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., dpc: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., enableBackground: bool = ..., ebg: bool = ..., enableKeyboardFocus: bool = ..., ekf: bool = ..., exists: bool = ..., ex: bool = ..., fullPathName: bool = ..., fpn: bool = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., hlc: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., io: bool = ..., manage: bool = ..., m: bool = ..., noBackground: bool = ..., nbg: bool = ..., node: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., numberOfPopupMenus: bool = ..., npm: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., pma: bool = ..., preventOverride: bool = ..., po: bool = ..., selectedColorControl: Optional[Union[str, bool]] = ..., sc: Optional[Union[str, bool]] = ..., selectedInterpControl: Optional[Union[str, bool]] = ..., si: Optional[Union[str, bool]] = ..., selectedPositionControl: Optional[Union[str, bool]] = ..., sp: Optional[Union[str, bool]] = ..., statusBarMessage: Optional[Union[str, bool]] = ..., sbm: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., verticalLayout: bool = ..., vl: bool = ..., visible: bool = ..., vis: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., vcc: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a control that displays an image representing
    the ramp node specified, and supports editing of that node.

    Args:
        annotation | ann: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor | bgc: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag | dtg: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback | dgc: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback | dpc: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable | en: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground | ebg: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus | ekf: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName | fpn: (query) - Return the full path name of the widget, which includes all the parents.
        height | h: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor | hlc: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        isObscured | io: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage | m: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground | nbg: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        node | n: (create) - Specifies the name of the newRamp texture node this port will represent.
        numberOfPopupMenus | npm: (query) - Return the number of popup menus attached to this control.
        parent | p: (create, query) - The parent layout for this control.
        popupMenuArray | pma: (query) - Return the names of all the popup menus attached to this control.
        preventOverride | po: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        selectedColorControl | sc: (create, edit) - Set the name of the control (if any) which is to be used to show the color of the currently selected entry in the ramp. This control will automatically update as the user selects different entries in the ramp, and will modify the selected entry if edited. The type of control must be an attrColorSliderGrp.
        selectedInterpControl | si: (create, edit) - Set the name of the control (if any) which is to be used to show the interpolation of the currently selected entry in the ramp. This control will automatically update as the user selects different entries in the ramp, and will modify the selected entry if edited. The type of control must be an attrEnumOptionMenuGrp.
        selectedPositionControl | sp: (create, edit) - Set the name of the control (if any) which is to be used to show the position of the currently selected entry in the ramp. This control will automatically update as the user selects different entries in the ramp, and will modify the selected entry if edited. The type of control must be an attrFieldSliderGrp.
        statusBarMessage | sbm: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        verticalLayout | vl: (create, edit, query) - Set the preview's layout.
        visible | vis: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand | vcc: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width | w: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def render(*args, abortMissingTexture: bool = ..., amt: bool = ..., batch: bool = ..., b: bool = ..., keepPreImage: bool = ..., kpi: bool = ..., layer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., nglowpass: bool = ..., ngl: bool = ..., nshadows: bool = ..., nsh: bool = ..., replace: bool = ..., rep: bool = ..., xresolution: Optional[Union[int, bool]] = ..., x: Optional[Union[int, bool]] = ..., yresolution: Optional[Union[int, bool]] = ..., y: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    The render command is used to start off a MayaSoftware rendering
    session of the currently active camera. If a rendering is already
    in progress, then this command stops the rendering. This command is
    not undoable.

    Args:
        abortMissingTexture | amt: (create) - Abort renderer when encountered missing texture. Only available when -batch is set
        batch | b: (create) - Run in batch mode. Compute the images for all renderable cameras. This is the mel equivalent of running maya in batch mode with the -render flag set. All other flags are ignored when -batch is used.
        keepPreImage | kpi: (create) - Keep the renderings prior to post-process around. Only available when -batch is set
        layer | l: (create) - Render the specified render layer. Only this render layer will be rendered, regardless of the renderable attribute value of the render layer. The layer name will be appended to the output image file name. The specified render layer becomes the current render layer before rendering, and remains as current render layer after the rendering.
        nglowpass | ngl: (create) - Overwrite glow pass capabilities (can turn off glow pass globally by setting this value to false)
        nshadows | nsh: (create) - Shadowing capabilities (can turn off shadow globally by setting this value to false)
        replace | rep: (create) - Replace the rendered image if it already exists. Only available when -batch is set
        xresolution | x: (create) - Overwrite x resolution
        yresolution | y: (create) - Overwrite y resolution
    """
    ...


def renderer(*args, addGlobalsNode: Optional[Union[str, bool]] = ..., agn: Optional[Union[str, bool]] = ..., addGlobalsTab: Optional[Union[Tuple[str, str, str], bool]] = ..., agt: Optional[Union[Tuple[str, str, str], bool]] = ..., batchRenderOptionsProcedure: Optional[Union[str, bool]] = ..., bro: Optional[Union[str, bool]] = ..., batchRenderOptionsStringProcedure: Optional[Union[str, bool]] = ..., bso: Optional[Union[str, bool]] = ..., batchRenderProcedure: Optional[Union[str, bool]] = ..., br: Optional[Union[str, bool]] = ..., cancelBatchRenderProcedure: Optional[Union[str, bool]] = ..., cbr: Optional[Union[str, bool]] = ..., changeIprRegionProcedure: Optional[Union[str, bool]] = ..., cir: Optional[Union[str, bool]] = ..., commandRenderProcedure: Optional[Union[str, bool]] = ..., cr: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., globalsNodes: bool = ..., gn: bool = ..., globalsTabCreateProcNames: bool = ..., gtc: bool = ..., globalsTabLabels: bool = ..., gtl: bool = ..., globalsTabUpdateProcNames: bool = ..., gtu: bool = ..., iprOptionsMenuLabel: Optional[Union[str, bool]] = ..., ipm: Optional[Union[str, bool]] = ..., iprOptionsProcedure: Optional[Union[str, bool]] = ..., io: Optional[Union[str, bool]] = ..., iprOptionsSubMenuProcedure: Optional[Union[str, bool]] = ..., ips: Optional[Union[str, bool]] = ..., iprRenderProcedure: Optional[Union[str, bool]] = ..., ipr: Optional[Union[str, bool]] = ..., iprRenderSubMenuProcedure: Optional[Union[str, bool]] = ..., irs: Optional[Union[str, bool]] = ..., isRunningIprProcedure: Optional[Union[str, bool]] = ..., isr: Optional[Union[str, bool]] = ..., logoCallbackProcedure: Optional[Union[str, bool]] = ..., lgc: Optional[Union[str, bool]] = ..., logoImageName: Optional[Union[str, bool]] = ..., log: Optional[Union[str, bool]] = ..., materialViewRendererList: bool = ..., mvl: bool = ..., materialViewRendererPause: bool = ..., mvp: bool = ..., materialViewRendererSuspend: bool = ..., mvs: bool = ..., namesOfAvailableRenderers: bool = ..., ava: bool = ..., pauseIprRenderProcedure: Optional[Union[str, bool]] = ..., psi: Optional[Union[str, bool]] = ..., polyPrelightProcedure: Optional[Union[str, bool]] = ..., pp: Optional[Union[str, bool]] = ..., refreshIprRenderProcedure: Optional[Union[str, bool]] = ..., rfi: Optional[Union[str, bool]] = ..., renderDiagnosticsProcedure: Optional[Union[str, bool]] = ..., rd: Optional[Union[str, bool]] = ..., renderGlobalsProcedure: Optional[Union[str, bool]] = ..., rg: Optional[Union[str, bool]] = ..., renderMenuProcedure: Optional[Union[str, bool]] = ..., rm: Optional[Union[str, bool]] = ..., renderOptionsProcedure: Optional[Union[str, bool]] = ..., ro: Optional[Union[str, bool]] = ..., renderProcedure: Optional[Union[str, bool]] = ..., r: Optional[Union[str, bool]] = ..., renderRegionProcedure: Optional[Union[str, bool]] = ..., rr: Optional[Union[str, bool]] = ..., renderSequenceProcedure: Optional[Union[str, bool]] = ..., rs: Optional[Union[str, bool]] = ..., rendererUIName: Optional[Union[str, bool]] = ..., ui: Optional[Union[str, bool]] = ..., renderingEditorsSubMenuProcedure: Optional[Union[str, bool]] = ..., res: Optional[Union[str, bool]] = ..., showBatchRenderLogProcedure: Optional[Union[str, bool]] = ..., brl: Optional[Union[str, bool]] = ..., showBatchRenderProcedure: Optional[Union[str, bool]] = ..., sbr: Optional[Union[str, bool]] = ..., showRenderLogProcedure: Optional[Union[str, bool]] = ..., srl: Optional[Union[str, bool]] = ..., startIprRenderProcedure: Optional[Union[str, bool]] = ..., sti: Optional[Union[str, bool]] = ..., stopIprRenderProcedure: Optional[Union[str, bool]] = ..., spi: Optional[Union[str, bool]] = ..., supportColorManagement: bool = ..., scm: bool = ..., textureBakingProcedure: Optional[Union[str, bool]] = ..., tb: Optional[Union[str, bool]] = ..., unregisterRenderer: bool = ..., unr: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to register renders.  This command allows you to
    specify the UI name and procedure names for renderers.
    The command also allow you to query the UI name and the procedure
    names for the registered renders.

    Args:
        addGlobalsNode | agn: (create, edit, query) - This flag allows the user to add a globals node the specified renderer uses.
        addGlobalsTab | agt: (create, edit) - Add a tab associated with the specified renderer for the unified render globals window.
        batchRenderOptionsProcedure | bro: (create, edit, query) - Set or query the batch render options procedure associated with the specified renderer.
        batchRenderOptionsStringProcedure | bso: (create, edit, query) - Set or query the argument string that will be used with the command line utility 'Render' when doing a batch render
        batchRenderProcedure | br: (create, edit, query) - Set or query the batch render procedure associated with the specified renderer.
        cancelBatchRenderProcedure | cbr: (create, edit, query) - Set or query returns the cancel batch render procedure associated with the specified renderer.
        changeIprRegionProcedure | cir: (create, edit, query) - Set or query the change IPR region procedure associated with the specified renderer.
        commandRenderProcedure | cr: (create, edit, query) - Set or query the command line rendering procedure associated with the specified renderer.
        exists | ex: (edit, query) - The flag returns true if the specified renderer is registered in the registry, and it returns false otherwise.
        globalsNodes | gn: (create, edit, query) - This flag returns the list of render globals nodes the specified renderer uses.
        globalsTabCreateProcNames | gtc: (create, edit, query) - This flag returns the names of procedures that are used to create the unified render globals window tabs that are associated with the specified renderer.
        globalsTabLabels | gtl: (create, edit, query) - This flag returns the labels of unified render globals window tabs that are associated with the specified renderer.
        globalsTabUpdateProcNames | gtu: (create, edit, query) - This flag returns the names of procedures that are used to update the unified render globals window tabs that are associated with the specified renderer.
        iprOptionsMenuLabel | ipm: (create, edit, query) - Set or query the label for the IPR update options menu which is under the render view's IPR menu.
        iprOptionsProcedure | io: (create, edit, query) - Set or query the IPR render options procedure associated with the specified renderer.
        iprOptionsSubMenuProcedure | ips: (create, edit, query) - Set or query the procedure for creating the sub menu for the IPR update options menu which is under the render view's IPR menu.
        iprRenderProcedure | ipr: (create, edit, query) - Set or query the IPR render command associated with the specified renderer.
        iprRenderSubMenuProcedure | irs: (create, edit, query) - Set or query the procedure for creating the sub menu for the IPR render menu which is under the render view's IPR menu.
        isRunningIprProcedure | isr: (create, edit, query) - Set or query the isRunningIpr command associated with the specified renderer.
        logoCallbackProcedure | lgc: (create, edit, query) - Set or query the procedure which is a callback associated to the logo for the specified renderer.   For example, the logo and the callback can be used in the unified render globals window beside the "Render Using" optionMenu.
        logoImageName | log: (create, edit, query) - Set or query the logo image name for the specified renderer. The logo is a image representing the renderer.
        materialViewRendererList | mvl: (edit, query) - Returns the names of material view renderers that are currently registered.
        materialViewRendererPause | mvp: (edit, query) - Specifies whether to pause the material viewer. Useful for globally halting updates to the material viewer. The material view renderer will remain suspended while the viewer is paused.
        materialViewRendererSuspend | mvs: (edit, query) - Specifies whether to suspend or resume the material view renderer. Useful for temporarily stopping the material view renderer while another rendering task is running.
        namesOfAvailableRenderers | ava: (edit, query) - Returns the names of renderers that are currently registered.
        pauseIprRenderProcedure | psi: (create, edit, query) - Set or query the pause IPR render procedure associated with the specified renderer.
        polyPrelightProcedure | pp: (create, edit, query) - Set or query the polygon prelight procedure associated with the specified renderer.
        refreshIprRenderProcedure | rfi: (create, edit, query) - Set or query the refresh IPR render procedure associated with the specified renderer.
        renderDiagnosticsProcedure | rd: (create, edit, query) - Set or query the render diagnostics procedure associated with the specified renderer.
        renderGlobalsProcedure | rg: (create, edit, query) - This flag is obsolete.  It will be removed in the next release.
        renderMenuProcedure | rm: (create, edit, query) - This flag is obsolete. It will be removed in the next release.
        renderOptionsProcedure | ro: (create, edit, query) - Set or query the render options procedure associated with the specified renderer.
        renderProcedure | r: (create, edit, query) - Set or query the render command associated with the specified renderer.
        renderRegionProcedure | rr: (create, edit, query) - Set or query the render region procedure associated with the specified renderer.
        renderSequenceProcedure | rs: (create, edit, query) - Set or query the sequence rendering procedure associated with the specified renderer.
        rendererUIName | ui: (create, edit, query) - Set or query the rendererUIName for the specified renderer. The rendererUIName is the name of the renderer as it would appear in menus.
        renderingEditorsSubMenuProcedure | res: (create, edit, query) - Set or query the procedure reponsible for creating renderer specific editors submenu under the "Rendering Editors" menu for the specified renderer.
        showBatchRenderLogProcedure | brl: (create, edit, query) - Set or query the log file batch procedure associated with the specified renderer.
        showBatchRenderProcedure | sbr: (create, edit, query) - Set or query the show batch render procedure associated with the specified renderer.
        showRenderLogProcedure | srl: (create, edit, query) - Set or query the log file render procedure associated with the specified renderer.
        startIprRenderProcedure | sti: (create, edit, query) - Set or query the start IPR render procedure associated with the specified renderer.
        stopIprRenderProcedure | spi: (create, edit, query) - Set or query the stop IPR render procedure associated with the specified renderer.
        supportColorManagement | scm: (edit, query) - Specifies whether the renderer supports color management.
        textureBakingProcedure | tb: (create, edit, query) - Set or query the texture baking procedure associated with the specified renderer.
        unregisterRenderer | unr: (edit, query) - Unregister the specified renderer.
    """
    ...


def renderGlobalsNode(*args, name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., renderQuality: Optional[Union[str, bool]] = ..., rq: Optional[Union[str, bool]] = ..., renderResolution: Optional[Union[str, bool]] = ..., rr: Optional[Union[str, bool]] = ..., shared: bool = ..., s: bool = ..., skipSelect: bool = ..., ss: bool = ...) -> Any:
    r"""
    This command creates a new node in the dependency graph of the
    specified type.
    
    The renderGlobalsNode creates a render globals node and registers it
    with the model. The createNode command will not register nodes of this
    type correctly.

    Args:
        name | n: (create) - Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.
        parent | p: (create) - Specifies the parent in the DAG under which the new node belongs.
        renderQuality | rq: (create) - Set the quality to be the renderQuality node with the given name.
        renderResolution | rr: (create) - Set the resolution to be the resolution node with the given name.
        shared | s: (create) - This node is shared across multiple files, so only create it if it does not already exist.
        skipSelect | ss: (create) - This node is not to be selected after creation, the original selection will be preserved.
    """
    ...


def renderInfo(*args, castShadows: bool = ..., cs: bool = ..., chordHeight: Optional[Union[float, bool]] = ..., ch: Optional[Union[float, bool]] = ..., chordHeightRatio: Optional[Union[float, bool]] = ..., chr: Optional[Union[float, bool]] = ..., doubleSided: bool = ..., ds: bool = ..., edgeSwap: bool = ..., es: bool = ..., minScreen: Optional[Union[float, bool]] = ..., ms: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., opposite: bool = ..., o: bool = ..., smoothShading: bool = ..., ss: bool = ..., unum: Optional[Union[int, bool]] = ..., un: Optional[Union[int, bool]] = ..., useChordHeight: bool = ..., uch: bool = ..., useChordHeightRatio: bool = ..., ucr: bool = ..., useDefaultLights: bool = ..., udl: bool = ..., useMinScreen: bool = ..., ums: bool = ..., utype: Optional[Union[int, bool]] = ..., ut: Optional[Union[int, bool]] = ..., vnum: Optional[Union[int, bool]] = ..., vn: Optional[Union[int, bool]] = ..., vtype: Optional[Union[int, bool]] = ..., vt: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The renderInfo commands sets geometric properties of surfaces
    of the selected object.

    Args:
        castShadows | cs: (create) - Determines if object casts shadow or not.
        chordHeight | ch: (create) - Tessellation subdivision criteria.
        chordHeightRatio | chr: (create) - Tessellation subdivision criteria.
        doubleSided | ds: (create) - Determines if object double or single sided.
        edgeSwap | es: (create) - Tessellation subdivision criteria.
        minScreen | ms: (create) - Tessellation subdivision criteria.
        name | n: (create) - Namespace to use.
        opposite | o: (create) - Determines if the normals of the object is to be reversed.
        smoothShading | ss: (create) - Determines if smooth shaded, or flat shaded - applies only to polysets.
        unum | un: (create) - Tessellation subdivision criteria.
        useChordHeight | uch: (create) - Tessellation subdivision criteria.
        useChordHeightRatio | ucr: (create) - Tessellation subdivision criteria.
        useDefaultLights | udl: (create) - Obsolete flag.
        useMinScreen | ums: (create) - Tessellation subdivision criteria.
        utype | ut: (create) - Tessellation subdivision criteria.
        vnum | vn: (create) - Tessellation subdivision criteria.
        vtype | vt: (create) - Tessellation subdivision criteria.
    """
    ...


def renderLayerPostProcess(*args, keepImages: bool = ..., ki: bool = ..., sceneName: Optional[Union[str, bool]] = ..., sn: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Post process the results when rendering is done with. Presently this
    generates a layered PSD file using individual iff files.

    Args:
        keepImages | ki: (create, query) - When set to on, the original iff images are kept after the conversion to PSD. Default is to remove them.
        sceneName | sn: (create, query) - Specifies the scene name for interactive batch rendering.
    """
    ...


def renderManip(*args, camera: Optional[Union[Tuple[bool, bool, bool, bool, bool], bool]] = ..., cam: Optional[Union[Tuple[bool, bool, bool, bool, bool], bool]] = ..., light: Optional[Union[Tuple[bool, bool, bool], bool]] = ..., lt: Optional[Union[Tuple[bool, bool, bool], bool]] = ..., spotLight: Optional[Union[Tuple[bool, bool, bool, bool, bool, bool, bool], bool]] = ..., slt: Optional[Union[Tuple[bool, bool, bool, bool, bool, bool, bool], bool]] = ..., state: bool = ..., st: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates manipulators for cameras or lights.

    Args:
        camera | cam: (edit, query) - Query or edit the visiblity status of the component camera manipulators. The order of components are: cycling index, center of interest, pivot, clipping planes, and unused.
        light | lt: (edit, query) - Query or edit the visiblity status of the component light manipulators. The order of components are: cycling index, center of interest, and pivot.
        spotLight | slt: (edit, query) - Query or edit the visiblity status of the component spot light manipulators. The order of components are: cycling index, center of interest, pivot, cone angle, penumbra, look through barn doors, and decay regions.
        state | st: (edit, query) - Query or edit the state of manipulators on an camera, ambient light, directional light, point light, or spot light. This flag's default value is on.
    """
    ...


def renderPartition(*args, query: bool = ...) -> Any:
    r"""
    Set or query the model's current partition. When flag q is
    not used, a partion name must be passed as an argument. In this
    case the current partition is set to that name.

    Args:
    """
    ...


def renderPassRegistry(*args, channels: Optional[Union[int, bool]] = ..., ch: Optional[Union[int, bool]] = ..., isPassSupported: bool = ..., ips: bool = ..., passID: Optional[Union[str, bool]] = ..., pi: Optional[Union[str, bool]] = ..., passName: bool = ..., pn: bool = ..., renderer: Optional[Union[str, bool]] = ..., r: Optional[Union[str, bool]] = ..., supportedChannelCounts: bool = ..., scc: bool = ..., supportedDataTypes: bool = ..., sdt: bool = ..., supportedPassSemantics: bool = ..., ps: bool = ..., supportedRenderPassNames: bool = ..., spn: bool = ..., supportedRenderPasses: bool = ..., srp: bool = ...) -> Any:
    r"""
    query information related with render passes.

    Args:
        channels | ch: (create) - Specify the number of channels for query.
        isPassSupported | ips: (create) - Return whether the pass is supported by the renderer This flag must be specified by the flag -passID firstly. The renderer whose default value is the current renderer is specified by the flag renderer.
        passID | pi: (create) - Specify the render pass ID for query.
        passName | pn: (create) - Get the pass name for the passID. This flag must be specified by the flag -passID firstly.
        renderer | r: (create) - Specify a renderer when using this command. By default the current renderer is specified.
        supportedChannelCounts | scc: (create) - List channel counts supported by the renderer(specified by the flag -renderer) and the specified pass ID. This flag must be specified by the flag -passID firstly.
        supportedDataTypes | sdt: (create) - List frame buffer types supported by the renderer(specified by the flag -renderer), the specified passID and channels. This flag must be specified by the flag -passID and -channels firstly.
        supportedPassSemantics | ps: (create) - List pass semantics supported by the specified passID. This flag must be specified by the flag -passId firstly.
        supportedRenderPassNames | spn: (create) - List render pass names supported by the renderer(specified by the flag -renderer).
        supportedRenderPasses | srp: (create) - List render passes supported by the renderer(specified by the flag -renderer).
    """
    ...


def renderQualityNode(*args, name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., shared: bool = ..., s: bool = ..., skipSelect: bool = ..., ss: bool = ...) -> Any:
    r"""
    This command creates a new node in the dependency graph of the
    specified type.
    
    The renderQualityNode creates a render quality node
    and registers it with the model.  The createNode
    command will not register nodes of this type correctly.

    Args:
        name | n: (create) - Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.
        parent | p: (create) - Specifies the parent in the DAG under which the new node belongs.
        shared | s: (create) - This node is shared across multiple files, so only create it if it does not already exist.
        skipSelect | ss: (create) - This node is not to be selected after creation, the original selection will be preserved.
    """
    ...


def renderSettings(*args, camera: Optional[Union[str, bool]] = ..., cam: Optional[Union[str, bool]] = ..., customTokenString: Optional[Union[str, bool]] = ..., cts: Optional[Union[str, bool]] = ..., firstImageName: bool = ..., fin: bool = ..., fullPath: bool = ..., fp: bool = ..., fullPathTemp: bool = ..., fpt: bool = ..., genericFrameImageName: Optional[Union[str, bool]] = ..., gin: Optional[Union[str, bool]] = ..., imageGenericName: bool = ..., ign: bool = ..., lastImageName: bool = ..., lin: bool = ..., layer: Optional[Union[str, bool]] = ..., lyr: Optional[Union[str, bool]] = ..., leaveUnmatchedTokens: bool = ..., lut: bool = ...) -> Any:
    r"""
    Query interface to the common tab of the render settings

    Args:
        camera | cam: (create) - Specify a camera that you want to replace the current renderable camera
        customTokenString | cts: (create) - Specify a custom key-value string to use to replace custom tokens in the file name. Use with firstImageName or lastImageName. Basic tokens (Scene, Layer, RenderLayer, Camera, Version, Extension) will be automatically expanded. Any other tokens must be specified here to be expanded. The format of the string is a space separated list of tokens-value pairs. For example, if the file name string is "myFile_<myToken>_<myOtherToken>_v" then the argument to this flag string should take the form "myToken=myTokenValue myOtherToken=myOtherTokenValue".
        firstImageName | fin: (create) - Returns the first image name
        fullPath | fp: (create) - Returns the full path for the image using the current project. Use with firstImageName, lastImageName, or genericFrameImageName.
        fullPathTemp | fpt: (create) - Returns the full path for the preview render of the image using the current project. Use with firstImageName, lastImageName, or genericFrameImageName.
        genericFrameImageName | gin: (create) - Returns the generic frame image name with the custom specified frame index token
        imageGenericName | ign: (create) - Returns the image generic name
        lastImageName | lin: (create) - Returns the last image name
        layer | lyr: (create) - Specify a render layer name that you want to replace the current render layer
        leaveUnmatchedTokens | lut: (create) - Do not remove unmatched tokens from the name string. Use with firstImageName or lastImageName.
    """
    ...


def renderThumbnailUpdate(*args, forceUpdate: Optional[Union[str, bool]] = ..., fu: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Toggle the updating of object thumbnails. These are visible in tools
    like the Attribute Editor and Hypershade. All thumbnails everywhere
    will not update to reflect changes to the object until this command is
    used to toggle to true unless a specific thumbnail is forced to render
    using the -forceUpdate flag.

    Args:
        forceUpdate | fu: (create) - Force the thumbnail to update.
    """
    ...


def renderWindowEditor(*args, autoResize: bool = ..., ar: bool = ..., blendMode: Optional[Union[int, bool]] = ..., blm: Optional[Union[int, bool]] = ..., caption: Optional[Union[str, bool]] = ..., cap: Optional[Union[str, bool]] = ..., changeCommand: Optional[Union[Tuple[str, str, str, str], bool]] = ..., cc: Optional[Union[Tuple[str, str, str, str], bool]] = ..., clear: Optional[Union[Tuple[int, int, float, float, float], bool]] = ..., cl: Optional[Union[Tuple[int, int, float, float, float], bool]] = ..., cmEnabled: bool = ..., cme: bool = ..., colorManage: bool = ..., com: bool = ..., compDisplay: Optional[Union[int, bool]] = ..., cd: Optional[Union[int, bool]] = ..., compImageFile: Optional[Union[str, bool]] = ..., cif: Optional[Union[str, bool]] = ..., control: bool = ..., ctl: bool = ..., currentCamera: Optional[Union[str, bool]] = ..., crc: Optional[Union[str, bool]] = ..., currentCameraRig: Optional[Union[str, bool]] = ..., crg: Optional[Union[str, bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., displayImage: Optional[Union[int, bool]] = ..., di: Optional[Union[int, bool]] = ..., displayImageViewCount: Optional[Union[int, bool]] = ..., dvc: Optional[Union[int, bool]] = ..., displayStyle: Optional[Union[str, bool]] = ..., dst: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., doubleBuffer: bool = ..., dbf: bool = ..., drawAxis: bool = ..., da: bool = ..., editorName: bool = ..., en: bool = ..., exists: bool = ..., ex: bool = ..., exposure: Optional[Union[float, bool]] = ..., exp: Optional[Union[float, bool]] = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., fmc: Optional[Union[str, bool]] = ..., frameImage: bool = ..., fi: bool = ..., frameRegion: bool = ..., fr: bool = ..., gamma: Optional[Union[float, bool]] = ..., ga: Optional[Union[float, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., hlc: Optional[Union[str, bool]] = ..., loadImage: str = ..., li: str = ..., lockMainConnection: bool = ..., lck: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., mlc: Optional[Union[str, bool]] = ..., marquee: Optional[Union[Tuple[float, float, float, float], bool]] = ..., mq: Optional[Union[Tuple[float, float, float, float], bool]] = ..., nbImages: bool = ..., nim: bool = ..., nextViewImage: bool = ..., nvi: bool = ..., outputColorManage: bool = ..., ocm: bool = ..., panel: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., pcaption: Optional[Union[str, bool]] = ..., pca: Optional[Union[str, bool]] = ..., realSize: bool = ..., rs: bool = ..., refresh: bool = ..., ref: bool = ..., removeAllImages: bool = ..., ra: bool = ..., removeImage: bool = ..., ri: bool = ..., resetRegion: bool = ..., rr: bool = ..., resetViewImage: bool = ..., rvi: bool = ..., saveImage: bool = ..., si: bool = ..., scaleBlue: Optional[Union[float, bool]] = ..., sb: Optional[Union[float, bool]] = ..., scaleGreen: Optional[Union[float, bool]] = ..., sg: Optional[Union[float, bool]] = ..., scaleRed: Optional[Union[float, bool]] = ..., sr: Optional[Union[float, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., slc: Optional[Union[str, bool]] = ..., showRegion: Optional[Union[Tuple[int, int], bool]] = ..., srg: Optional[Union[Tuple[int, int], bool]] = ..., singleBuffer: bool = ..., sbf: bool = ..., snapshot: Optional[Union[Tuple[str, int, int], bool]] = ..., snp: Optional[Union[Tuple[str, int, int], bool]] = ..., snapshotMode: bool = ..., snm: bool = ..., stateString: bool = ..., sts: bool = ..., stereo: Optional[Union[int, bool]] = ..., s: Optional[Union[int, bool]] = ..., stereoImageOrientation: Optional[Union[Tuple[str, str], bool]] = ..., sio: Optional[Union[Tuple[str, str], bool]] = ..., stereoMode: Optional[Union[str, bool]] = ..., sm: Optional[Union[str, bool]] = ..., toggle: bool = ..., tgl: bool = ..., unParent: bool = ..., up: bool = ..., unlockMainConnection: bool = ..., ulk: bool = ..., updateMainConnection: bool = ..., upd: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., viewImageCount: Optional[Union[int, bool]] = ..., vic: Optional[Union[int, bool]] = ..., viewTransformName: Optional[Union[str, bool]] = ..., vtn: Optional[Union[str, bool]] = ..., writeImage: str = ..., wi: str = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a editor window that can receive the result of the
    rendering process

    Args:
        autoResize | ar: (create, edit, query) - Lets the render view editor automatically resize the viewport or not.
        blendMode | blm: (create, edit, query) - Sets the blend mode for the render view. New image sent to the render view will be blended with the previous image in the render view, and the composited image will appear.
        caption | cap: (create, edit, query) - Sets the caption which appears at the bottom of the render view.
        changeCommand | cc: (create, edit, query) - Parameters:  First string: command Second string: editorName Third string: editorCmd Fourth string: updateFunc   Call the command when something changes in the editor The command should have this prototype :  command(string $editor, string $editorCmd, string $updateFunc, int $reason)  The possible reasons could be :  0: no particular reason 1: scale color 2: buffer (single/double) 3: axis  4: image displayed 5: image saved in memory
        clear | cl: (create, edit, query) - Clear the image with the given color at the given resolution. Arguments are respectively: width height red green blue.
        cmEnabled | cme: (edit, query) - Turn on or off applying color management in the View.  If set, the color management configuration set in the current view is used.
        colorManage | com: (edit) - When used with the writeImage flag, causes the written image to be color-managed using the settings from the view color manager attached to the view.
        compDisplay | cd: (create, edit, query) - 0 : disable compositing. 1 : displays the composited image immediately. For example, when foreground layer tile is sent to the render view window, the composited tile is displayed in the render view window, and the original foreground layer tile is not displayed. 2 : display the un-composited image, and keep the composited image for the future command. For example, when foreground layer tile is sent to the render view window, the original foreground layer tile is not displayed, and the composited tile is stored in a buffer. 3 : show the current composited image. If there is a composited image in the buffer, display it.
        compImageFile | cif: (create, edit, query) - Open the given image file and blend with the buffer as if the image was just rendered.
        control | ctl: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        currentCamera | crc: (create, edit, query) - Get or set the current camera. (used when redoing last render)
        currentCameraRig | crg: (create, edit, query) - Get or set the current camera rig name. If a camera rig is specified, it will be used when redoing the last render as opposed to the currentCamera value, as the currentCamera value will hold the child camera last used for rendering the camera rig.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        displayImage | di: (edit, query) - Set a particular image in the Editor Image Stack as the current Editor Image. Images are added to the Editor Image Stack using the "si/saveImage" flag.
        displayImageViewCount | dvc: (query) - Query the number of views stored for a given image in the Editor Image Stack. This is not the same as querying using "viewImageCount" which returns the number of views for the current rendered image.
        displayStyle | dst: (create, edit, query) - Set the mode to display the image. Valid values are:  "color" to display the basic RGB image "mask" to display the mask channel "lum" to display the luminance of the image
        docTag | dtg: (create, edit, query) - Attaches a tag to the editor.
        doubleBuffer | dbf: (create, edit, query) - Set the display in double buffer mode
        drawAxis | da: (create, edit, query) - Set or query whether the axis will be drawn.
        editorName | en: (query) - Returns the name of the editor, or an empty string if the editor has not been created yet.
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        exposure | exp: (edit, query) - The exposure value used by the color management of the current view.
        filter | f: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection | fmc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        frameImage | fi: (create, edit, query) - Frames the image inside the window.
        frameRegion | fr: (create, edit, query) - Frames the region inside the window.
        gamma | ga: (edit, query) - The gamma value used by the color management of the current view.
        highlightConnection | hlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        loadImage | li: (edit) - load an image from disk and set it as the current Editor Image
        lockMainConnection | lck: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        mainListConnection | mlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        marquee | mq: (create, edit, query) - The arguments define the four corners of a rectangle: top left bottom right. The rectangle defines a marquee for the render computation.
        nbImages | nim: (query) - returns the number of images
        nextViewImage | nvi: (create, edit) - The render editor has the capability to render multiple cameras within a single view. This is different from image binning where an image is saved. Multiple image views are useful for comparing two different camera renders side-by-side. The nextViewImage flag tells the editor that it should prepare its internal image storage mechanism to store to the next view location.
        outputColorManage | ocm: (edit) - When used with the writeImage flag, causes the written image to be color-managed using the outpute color space in the color preferences attached to the view.
        panel | pnl: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent | p: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        pcaption | pca: (create, edit, query) - Get or set the permanent caption which appears under the image that is currently showing in the render editor.
        realSize | rs: (create, edit, query) - Display the image with a one to one pixel match.
        refresh | ref: (edit) - requests a refresh of the current Editor Image.
        removeAllImages | ra: (edit) - remove all the Editor Images from the Editor Image Stack
        removeImage | ri: (edit) - remove the current Editor Image from the Editor Image Stack
        resetRegion | rr: (create, edit, query) - Forces a reset of any marquee/region.
        resetViewImage | rvi: (create, edit) - The render editor has the capability to render multiple cameras within a single view. This is different from image binning where an image is saved. Multiple image views are useful for comparing two different camera renders side-by-side. The resetViewImage flag tells the editor that it should reset its internal image storage mechanism to the first image. This would happen at the very start of a render view render.
        saveImage | si: (edit) - save the current Editor Image to memory. Saved Editor Images are stored in an Editor Image Stack. The most recently saved image is stored in position 0, the second most recently saved image in position 1, and so on... To set the current Editor Image to a previously saved image use the "di/displayImage" flag.
        scaleBlue | sb: (create, edit, query) - Define the scaling factor for the blue component in the View. The default value is 1 and can be between -1000 to +1000
        scaleGreen | sg: (create, edit, query) - Define the scaling factor for the green component in the View. The default value is 1 and can be between -1000 to +1000
        scaleRed | sr: (create, edit, query) - Define the scaling factor for the red component in the View. The default value is 1 and can be between -1000 to +1000
        selectionConnection | slc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        showRegion | srg: (create, edit, query) - Shows the current region at the given resolution. The two parameters define the width and height.
        singleBuffer | sbf: (create, edit, query) - Set the display in single buffer mode
        snapshot | snp: (create, edit, query) - Makes a copy of the camera of the model editor at the given size. First argument is the editor name, second is the width, third is the height.
        snapshotMode | snm: (create, edit, query) - Get or set the window's snapshot mode.
        stateString | sts: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        stereo | s: (create, edit, query) - Puts the editor into stereo image mode.  The effective resolution of the output image is twice the size of the horizontal size. The orientation of the images can be set using the stereoOrientation flag.
        stereoImageOrientation | sio: (create, edit, query) - Specifies the orientation of stereo camera renders.  The first argument specifies the orientation value for the firstleft image and the second argument specifies the orientation value for the right image. The orientation values are 'normal', the image appears as seen throught he camera, or 'mirrored', the image is mirrored horizontally.
        stereoMode | sm: (create, edit, query) - Specifies how the image is displayed in the view.  By default the stereo is rendered with a side by side image.  The rendered image is a single image that is twice the size of a normal image, 'both'. Users can also choose to display as 'redcyan', 'redcyanlum', 'leftonly', 'rightonly', or 'stereo'.  both - displays both the left and right redcyan - displays the images as a red/cyan pair. redcyanlum - displays the luminance of the images as a red/cyan pair. leftonly - displays the left side only rightonly - displays the right side only stereo - mode that supports Crystal Eyes(tm) or Zscreen (tm) renders
        toggle | tgl: (create, edit, query) - Turns the ground plane display on/off.
        unParent | up: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection | ulk: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection | upd: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        viewImageCount | vic: (create, edit, query) - The render editor has the capability to render multiple cameras within a single view. This is different from image binning where an image is saved. Multiple image views are useful for comparing two different camera renders side-by-side. The viewImageCount flag tells the editor that it should prepare its internal image storage mechanism for a given number of views.
        viewTransformName | vtn: (edit, query) - Sets/gets the view transform to be applied if color management is enabled in the current view.
        writeImage | wi: (edit) - write the current Editor Image to disk
    """
    ...


def resolutionNode(*args, name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., shared: bool = ..., s: bool = ..., skipSelect: bool = ..., ss: bool = ...) -> Any:
    r"""
    This command creates a new node in the dependency graph of the
    specified type.
    
    The resolutionNode creates a render resolution node
    and registers it with the model.  The createNode
    command will not register nodes of this type correctly.

    Args:
        name | n: (create) - Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.
        parent | p: (create) - Specifies the parent in the DAG under which the new node belongs.
        shared | s: (create) - This node is shared across multiple files, so only create it if it does not already exist.
        skipSelect | ss: (create) - This node is not to be selected after creation, the original selection will be preserved.
    """
    ...


def roll(*args, absolute: bool = ..., abs: bool = ..., degree: Optional[Union[float, bool]] = ..., d: Optional[Union[float, bool]] = ..., relative: bool = ..., rel: bool = ...) -> Any:
    r"""
    The roll command rotates a camera about its viewing direction, a
    positive angle produces clockwise camera rotation, while a
    negative angle produces counter-clockwise camera rotation.
    
    The default mode is relative and the rotation is applied with
    respect to the current orientation of the camera. When mode is set
    to absolute, the rotation is applied with respect to the plane
    constructed from the following three vectors in the world space:
    the world up vector, the camera view vector, and the camera up
    vector.
    
    The rotation angle is specified in degrees.
    
    The roll command can be applied to either a perspective or an
    orthographic camera.
    
    This command may be applied to more than one camera; objects that
    are not cameras are ignored. When no camera name supplied, this command
    is applied to all currently active cameras.

    Args:
        absolute | abs: (create) - Set to absolute mode.
        degree | d: (create) - Set the amount of the rotation angle.
        relative | rel: (create) - Set to relative mode.
    """
    ...


def sampleImage(*args, fastSample: bool = ..., f: bool = ..., resolution: Optional[Union[Tuple[int, str], bool]] = ..., r: Optional[Union[Tuple[int, str], bool]] = ...) -> Any:
    r"""
    The sampleImage command is used to control parameters of
    sample images, such as swatches in the multilister.
    The fast option turns on or off some rendering cheats which speed up the
    render but may cause edges to look ragged.
    The resolution option specifies the width in pixels of the image which will
    be rendered for the specified node. Note that the width of the image
    is also the height of the image since sample images are square.

    Args:
        fastSample | f: (create) - If fast but rough rendering for sampleImage is to be used
        resolution | r: (create) - The first argument to this flag specifies a resolution in pixels. The second argument specifies a dependency node. The effect of this flag is that further sample image renderings for the specified node will be made at the specified resolution.
    """
    ...


def setDefaultShadingGroup(*args, query: bool = ...) -> Any:
    r"""
    The setDefaultShadingGroup command is used to change which shading
    group is considered the current default shading group. Subsequently
    created objects will be assigned to the new default group.

    Args:
    """
    ...


def setRenderPassType(*args, defaultDataType: bool = ..., d: bool = ..., numChannels: Optional[Union[int, bool]] = ..., n: Optional[Union[int, bool]] = ..., type: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command will set the passID of a renderPass node and
    create the custom attributes specified by the corresponding render pass
    definition.  If the render pass
    node already has a passID assigned to it, attributes that are no longer
    required become hidden, and new attributes are unhidden and/or created as
    needed.  This allows passIDs to be changed back and forth without losing
    attribute data.  It also allows common attributes to be transported from one
    render pass type to another.

    Args:
        defaultDataType | d: (create) - If set, the render pass will use its default data type.
        numChannels | n: (create) - Specify the number of channels to use in the render pass. Note that this flag is only valid if there is an implementation supporting the requested number of channels.
        type | t: (create) - Specify the pass type to assign to the pass node(s).
    """
    ...


def shadingConnection(*args, connectionState: bool = ..., cs: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Sets the connection state of a connection between nodes that are used
    in shading. Specify the destination attribute of the connection.

    Args:
        connectionState | cs: (create, edit, query) - Specifies the state of the connection. On/True/1 means the connection is still active. Off/False/0 means the connection is inactive.
    """
    ...


def shadingNetworkCompare(*args, byName: bool = ..., nam: bool = ..., byValue: bool = ..., val: bool = ..., delete: bool = ..., equivalent: bool = ..., eq: bool = ..., network1: bool = ..., n1: bool = ..., network2: bool = ..., n2: bool = ..., upstreamOnly: bool = ..., up: bool = ..., query: bool = ...) -> Any:
    r"""
    This command allows you to compare two shading networks.

    Args:
        byName | nam: (create) - Indicates whether the comparison should consider node names. If true, two shading networks will be considered equivalent only if the names of corresponding nodes are the same, ignoring namespaces. If false, two shading networks will be considered equivalent even if corresponding nodes are named differently. Default is 'false'.
        byValue | val: (create) - Indicates whether the comparison should consider the values of unconnected attributes. If true, two shading networks will be considered equivalent only if corresponding, unconnected attributes are the same type and have the same value. Only attributes of type 'int', 'bool', 'float', and 'string' will have their values compared. If false, two shading networks will be considered equivalent even if corresponding, unconnected attributes have different values or are different types. Default is 'true'.
        delete | delete: (create) - Deletes the specified comparison from memory.
        equivalent | eq: (query) - Returns an int. 1 if the shading networks in the specified comparison are equivalent. 0 otherwise.
        network1 | n1: (query) - Returns a string[]. Returns an empty string array if the shading networks in the specified comparison are not equivalent. Otherwise returns the nodes in the first shading network.
        network2 | n2: (query) - Returns a string[]. Returns an empty string array if the shading networks in the specified comparison are not equivalent. Otherwise returns the nodes in the second shading network.
        upstreamOnly | up: (create) - Indicates whether the comparison should consider nodes which are connected downstream from shading network nodes. If true, only those nodes which are upstream from the shading group will be considered. If, following only downstream connections, there is no connection path from a node to one of the shader attributes on the shading group, the node will not be considered. If false, a node will be considered if a connection path can found, following either upstream or downstream connections, which terminates with an input connection to one of the shading groups shader attributes. These dangling nodes do not directly contribute to the color, displacement, or volume characteristics of the shading group. Default is 'false'.
    """
    ...


def shadingNode(*args, asLight: bool = ..., al: bool = ..., asPostProcess: bool = ..., app: bool = ..., asRendering: bool = ..., ar: bool = ..., asShader: bool = ..., asTexture: bool = ..., at: bool = ..., asUtility: bool = ..., au: bool = ..., isColorManaged: bool = ..., icm: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., shared: bool = ..., s: bool = ..., skipSelect: bool = ..., ss: bool = ...) -> Any:
    r"""
    This command creates a new node in the dependency graph of the
    specified type.
    
    The shadingNode command classifies any DG node as a shader, texture
    light, post process, or utility so that it can be properly organized
    in the multi-lister.  Recall that any DG node can be used a part of a
    a shader, texture or light - regardless of how it is classified by this.
    command. These classifications are provided for convenience in the UI.

    Args:
        asLight | al: (create) - classify the current DG node as a light
        asPostProcess | app: (create) - classify the current DG node as a post process
        asRendering | ar: (create) - classify the current DG node as a rendering node
        asShader | asShader: (create) - classify the current DG node as a shader
        asTexture | at: (create) - classify the current DG node as a texture
        asUtility | au: (create) - classify the current DG node as a utility
        isColorManaged | icm: (create) - classify the current DG node as being color managed
        name | n: (create) - Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.
        parent | p: (create) - Specifies the parent in the DAG under which the new node belongs.
        shared | s: (create) - This node is shared across multiple files, so only create it if it does not already exist.
        skipSelect | ss: (create) - This node is not to be selected after creation, the original selection will be preserved.
    """
    ...


def showShadingGroupAttrEditor(*args, query: bool = ...) -> Any:
    r"""
    The showShadingGroupAttrEditor command opens up the attribute
    editor for the current object's shading-group information.

    Args:
    """
    ...


def soloMaterial(*args, attr: Optional[Union[str, bool]] = ..., a: Optional[Union[str, bool]] = ..., last: bool = ..., l: bool = ..., node: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., unsolo: bool = ..., us: bool = ..., query: bool = ...) -> Any:
    r"""
    Shows a preview of a specified material node output attribute.

    Args:
        attr | a: (create, query) - The attr flag specifies a node attribute to solo.
        last | l: (create, query) - Whether to solo the last material node and attribute.
        node | n: (create, query) - The node flag specifies the node to solo.
        unsolo | us: (create, query) - Whether to remove soloing.
    """
    ...


def spotLight(*args, barnDoors: bool = ..., bd: bool = ..., bottomBarnDoorAngle: Optional[Union[float, bool]] = ..., bbd: Optional[Union[float, bool]] = ..., coneAngle: Optional[Union[float, bool]] = ..., ca: Optional[Union[float, bool]] = ..., decayRate: Optional[Union[int, bool]] = ..., d: Optional[Union[int, bool]] = ..., discRadius: Optional[Union[float, bool]] = ..., drs: Optional[Union[float, bool]] = ..., dropOff: Optional[Union[float, bool]] = ..., do: Optional[Union[float, bool]] = ..., exclusive: bool = ..., exc: bool = ..., intensity: Optional[Union[float, bool]] = ..., i: Optional[Union[float, bool]] = ..., leftBarnDoorAngle: Optional[Union[float, bool]] = ..., lbd: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., penumbra: Optional[Union[float, bool]] = ..., p: Optional[Union[float, bool]] = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., pos: Optional[Union[Tuple[float, float, float], bool]] = ..., rgb: Optional[Union[Tuple[float, float, float], bool]] = ..., rightBarnDoorAngle: Optional[Union[float, bool]] = ..., rbd: Optional[Union[float, bool]] = ..., rotation: Optional[Union[Tuple[float, float, float], bool]] = ..., rot: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowColor: Optional[Union[Tuple[float, float, float], bool]] = ..., sc: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowDither: Optional[Union[float, bool]] = ..., sd: Optional[Union[float, bool]] = ..., shadowSamples: Optional[Union[int, bool]] = ..., sh: Optional[Union[int, bool]] = ..., softShadow: bool = ..., ss: bool = ..., topBarnDoorAngle: Optional[Union[float, bool]] = ..., tbd: Optional[Union[float, bool]] = ..., useRayTraceShadows: bool = ..., rs: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    TlightCmd is the base class for other light commands.
    TnonAmbientLightCmd is a class that looks like a command but
    is not.  It is a base class for the extended/nonExtended
    lights.
    TnonExtendedLightCmd is a base class and not a real command. It is inherited by several
    lights: TpointLight, TdirectionalLight, TspotLight etc.
    The spotLight command is used to edit the parameters of
    existing spotLights, or to create new ones. The default
    behaviour is to create a new spotlight.

    Args:
        barnDoors | bd: (create, edit, query) - Are the barn doors enabled?
        bottomBarnDoorAngle | bbd: (create, edit, query) - Angle of the bottom of the barn door.
        coneAngle | ca: (create, edit, query) - angle of the spotLight
        decayRate | d: (create) - Decay rate of the light (0-no decay, 1-slow, 2-realistic, 3-fast)
        discRadius | drs: (create, query) - Radius of shadow disc.
        dropOff | do: (create, edit, query) - dropOff of the spotLight
        exclusive | exc: (create, query) - True if the light is exclusively assigned
        intensity | i: (create, query) - Intensity of the light
        leftBarnDoorAngle | lbd: (create, edit, query) - Angle of the left of the barn door.
        name | n: (create, query) - Name of the light
        penumbra | p: (create, edit, query) - specify penumbra region
        position | pos: (create, query) - Position of the light
        rgb | rgb: (create, query) - RGB colour of the light
        rightBarnDoorAngle | rbd: (create, edit, query) - Angle of the right of the barn door.
        rotation | rot: (create, query) - Rotation of the light for orientation, where applicable
        shadowColor | sc: (create, query) - Color of the light's shadow
        shadowDither | sd: (create, query) - Shadow dithering value.
        shadowSamples | sh: (create, query) - Numbr of shadow samples to use
        softShadow | ss: (create, query) - True if soft shadowing is to be enabled
        topBarnDoorAngle | tbd: (create, edit, query) - Angle of the top of the barn door.
        useRayTraceShadows | rs: (create, query) - True if ray trace shadows are to be used
    """
    ...


def spotLightPreviewPort(*args, annotation: Optional[Union[str, bool]] = ..., ann: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., bgc: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dgc: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., dpc: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., enableBackground: bool = ..., ebg: bool = ..., enableKeyboardFocus: bool = ..., ekf: bool = ..., exists: bool = ..., ex: bool = ..., fullPathName: bool = ..., fpn: bool = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., hlc: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., io: bool = ..., manage: bool = ..., m: bool = ..., noBackground: bool = ..., nbg: bool = ..., numberOfPopupMenus: bool = ..., npm: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., pma: bool = ..., preventOverride: bool = ..., po: bool = ..., spotLight: Optional[Union[str, bool]] = ..., sl: Optional[Union[str, bool]] = ..., statusBarMessage: Optional[Union[str, bool]] = ..., sbm: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., visible: bool = ..., vis: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., vcc: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., widthHeight: Optional[Union[Tuple[int, int], bool]] = ..., wh: Optional[Union[Tuple[int, int], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a 3dPort that displays an image representing the
    illumination provided by the spotLight. It is a picture of a plane
    being illuminated by a light.
    
    The optional argument is the name of the 3dPort.

    Args:
        annotation | ann: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor | bgc: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag | dtg: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback | dgc: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback | dpc: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable | en: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground | ebg: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus | ekf: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName | fpn: (query) - Return the full path name of the widget, which includes all the parents.
        height | h: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor | hlc: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        isObscured | io: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage | m: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground | nbg: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfPopupMenus | npm: (query) - Return the number of popup menus attached to this control.
        parent | p: (create, query) - The parent layout for this control.
        popupMenuArray | pma: (query) - Return the names of all the popup menus attached to this control.
        preventOverride | po: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        spotLight | sl: (create) - Name of the spotLight.
        statusBarMessage | sbm: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        visible | vis: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand | vcc: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width | w: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        widthHeight | wh: (create) - The width and height of the port.
    """
    ...


def stereoCameraView(*args, activeComponentsXray: bool = ..., acx: bool = ..., activeCustomEnvironment: str = ..., ace: str = ..., activeCustomGeometry: Optional[Union[str, bool]] = ..., acg: Optional[Union[str, bool]] = ..., activeCustomLighSet: Optional[Union[str, bool]] = ..., acl: Optional[Union[str, bool]] = ..., activeCustomOverrideGeometry: Optional[Union[str, bool]] = ..., aog: Optional[Union[str, bool]] = ..., activeCustomRenderer: Optional[Union[str, bool]] = ..., acr: Optional[Union[str, bool]] = ..., activeOnly: bool = ..., ao: bool = ..., activeShadingGraph: Optional[Union[str, bool]] = ..., asg: Optional[Union[str, bool]] = ..., activeSupported: bool = ..., ams: bool = ..., activeView: bool = ..., av: bool = ..., addObjects: str = ..., aob: str = ..., addSelected: bool = ..., allObjects: bool = ..., alo: bool = ..., backfaceCulling: bool = ..., bfc: bool = ..., bluePencil: bool = ..., bp: bool = ..., bufferMode: Optional[Union[str, bool]] = ..., bm: Optional[Union[str, bool]] = ..., bumpResolution: Optional[Union[Tuple[int, int], bool]] = ..., brz: Optional[Union[Tuple[int, int], bool]] = ..., camera: Optional[Union[str, bool]] = ..., cam: Optional[Union[str, bool]] = ..., cameraName: Optional[Union[str, bool]] = ..., cn: Optional[Union[str, bool]] = ..., cameraSet: Optional[Union[str, bool]] = ..., cst: Optional[Union[str, bool]] = ..., cameraSetup: bool = ..., cs: bool = ..., cameras: bool = ..., ca: bool = ..., capture: Optional[Union[str, bool]] = ..., cpt: Optional[Union[str, bool]] = ..., captureSequenceNumber: Optional[Union[int, bool]] = ..., csn: Optional[Union[int, bool]] = ..., centerCamera: Optional[Union[str, bool]] = ..., ccm: Optional[Union[str, bool]] = ..., colorMap: bool = ..., cm: bool = ..., colorResolution: Optional[Union[Tuple[int, int], bool]] = ..., crz: Optional[Union[Tuple[int, int], bool]] = ..., control: bool = ..., ctl: bool = ..., controlVertices: bool = ..., cv: bool = ..., cullingOverride: Optional[Union[str, bool]] = ..., cov: Optional[Union[str, bool]] = ..., default: bool = ..., d: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., deformers: bool = ..., df: bool = ..., dimensions: bool = ..., dim: bool = ..., displayAppearance: Optional[Union[str, bool]] = ..., da: Optional[Union[str, bool]] = ..., displayLights: Optional[Union[str, bool]] = ..., dl: Optional[Union[str, bool]] = ..., displayMode: Optional[Union[str, bool]] = ..., dm: Optional[Union[str, bool]] = ..., displayTextures: bool = ..., dtx: bool = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., dynamicConstraints: bool = ..., dc: bool = ..., dynamics: bool = ..., dy: bool = ..., editorChanged: Optional[Union[str, bool]] = ..., ec: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., filteredObjectList: bool = ..., fol: bool = ..., fluids: bool = ..., fl: bool = ..., fogColor: Optional[Union[Tuple[float, float, float, float], bool]] = ..., fcl: Optional[Union[Tuple[float, float, float, float], bool]] = ..., fogDensity: Optional[Union[float, bool]] = ..., fdn: Optional[Union[float, bool]] = ..., fogEnd: Optional[Union[float, bool]] = ..., fen: Optional[Union[float, bool]] = ..., fogMode: Optional[Union[str, bool]] = ..., fmd: Optional[Union[str, bool]] = ..., fogSource: Optional[Union[str, bool]] = ..., fsc: Optional[Union[str, bool]] = ..., fogStart: Optional[Union[float, bool]] = ..., fst: Optional[Union[float, bool]] = ..., fogging: bool = ..., fg: bool = ..., follicles: bool = ..., fo: bool = ..., forceMainConnection: Optional[Union[str, bool]] = ..., fmc: Optional[Union[str, bool]] = ..., grid: bool = ..., gr: bool = ..., hairSystems: bool = ..., hs: bool = ..., handles: bool = ..., ha: bool = ..., headsUpDisplay: bool = ..., hud: bool = ..., height: bool = ..., h: bool = ..., highlightConnection: Optional[Union[str, bool]] = ..., hlc: Optional[Union[str, bool]] = ..., hulls: bool = ..., hu: bool = ..., ignorePanZoom: bool = ..., ipz: bool = ..., ikHandles: bool = ..., ikh: bool = ..., imagePlane: bool = ..., imp: bool = ..., interactive: bool = ..., i: bool = ..., interactiveBackFaceCull: bool = ..., ibc: bool = ..., interactiveDisableShadows: bool = ..., dis: bool = ..., isFiltered: bool = ..., jointXray: bool = ..., jx: bool = ..., joints: bool = ..., j: bool = ..., leftCamera: Optional[Union[str, bool]] = ..., lcm: Optional[Union[str, bool]] = ..., lights: bool = ..., lt: bool = ..., lineWidth: Optional[Union[float, bool]] = ..., lw: Optional[Union[float, bool]] = ..., locators: bool = ..., lc: bool = ..., lockMainConnection: bool = ..., lck: bool = ..., lowQualityLighting: bool = ..., lql: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., mlc: Optional[Union[str, bool]] = ..., manipulators: bool = ..., m: bool = ..., maxConstantTransparency: Optional[Union[float, bool]] = ..., mct: Optional[Union[float, bool]] = ..., maximumNumHardwareLights: bool = ..., mhl: bool = ..., modelPanel: Optional[Union[str, bool]] = ..., mp: Optional[Union[str, bool]] = ..., motionTrails: bool = ..., mt: bool = ..., nCloths: bool = ..., ncl: bool = ..., nParticles: bool = ..., npa: bool = ..., nRigids: bool = ..., nr: bool = ..., noUndo: bool = ..., nud: bool = ..., nurbsCurves: bool = ..., nc: bool = ..., nurbsSurfaces: bool = ..., ns: bool = ..., objectFilter: Optional[Union[str, bool]] = ..., obf: Optional[Union[str, bool]] = ..., objectFilterList: Optional[Union[str, bool]] = ..., ofl: Optional[Union[str, bool]] = ..., objectFilterListUI: Optional[Union[str, bool]] = ..., ofu: Optional[Union[str, bool]] = ..., objectFilterShowInHUD: bool = ..., ofs: bool = ..., objectFilterUI: Optional[Union[str, bool]] = ..., obu: Optional[Union[str, bool]] = ..., occlusionCulling: bool = ..., ocl: bool = ..., panel: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., pivots: bool = ..., pv: bool = ..., planes: bool = ..., pl: bool = ..., pluginObjects: Tuple[str, bool] = ..., po: Tuple[str, bool] = ..., pluginShapes: bool = ..., ps: bool = ..., polymeshes: bool = ..., pm: bool = ..., queryPluginObjects: Optional[Union[str, bool]] = ..., qpo: Optional[Union[str, bool]] = ..., removeSelected: bool = ..., rs: bool = ..., rendererDeviceName: bool = ..., rdn: bool = ..., rendererList: bool = ..., rls: bool = ..., rendererListUI: bool = ..., rlu: bool = ..., rendererName: Optional[Union[str, bool]] = ..., rnm: Optional[Union[str, bool]] = ..., rendererOverrideList: bool = ..., rol: bool = ..., rendererOverrideListUI: bool = ..., rou: bool = ..., rendererOverrideName: Optional[Union[str, bool]] = ..., rom: Optional[Union[str, bool]] = ..., resetCustomCamera: bool = ..., rcc: bool = ..., rigRoot: Optional[Union[str, bool]] = ..., rr: Optional[Union[str, bool]] = ..., rightCamera: Optional[Union[str, bool]] = ..., rcm: Optional[Union[str, bool]] = ..., sceneRenderFilter: Optional[Union[str, bool]] = ..., srf: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., slc: Optional[Union[str, bool]] = ..., selectionHiliteDisplay: bool = ..., sel: bool = ..., setSelected: bool = ..., ss: bool = ..., shadingModel: Optional[Union[int, bool]] = ..., sml: Optional[Union[int, bool]] = ..., shadows: bool = ..., sdw: bool = ..., smallObjectCulling: bool = ..., soc: bool = ..., smallObjectThreshold: Optional[Union[float, bool]] = ..., sot: Optional[Union[float, bool]] = ..., smoothWireframe: bool = ..., swf: bool = ..., sortTransparent: bool = ..., st: bool = ..., stateString: bool = ..., sts: bool = ..., stereoDrawMode: bool = ..., sdm: bool = ..., strokes: bool = ..., str: bool = ..., subdivSurfaces: bool = ..., sds: bool = ..., swapEyes: bool = ..., se: bool = ..., textureAnisotropic: bool = ..., ta: bool = ..., textureCompression: bool = ..., tcp: bool = ..., textureDisplay: Optional[Union[str, bool]] = ..., td: Optional[Union[str, bool]] = ..., textureEnvironmentMap: bool = ..., tem: bool = ..., textureHilight: bool = ..., th: bool = ..., textureMaxSize: Optional[Union[int, bool]] = ..., tms: Optional[Union[int, bool]] = ..., textureMemoryUsed: bool = ..., tmu: bool = ..., textureSampling: Optional[Union[int, bool]] = ..., ts: Optional[Union[int, bool]] = ..., textures: bool = ..., tx: bool = ..., transpInShadows: bool = ..., tis: bool = ..., transparencyAlgorithm: Optional[Union[str, bool]] = ..., tal: Optional[Union[str, bool]] = ..., twoSidedLighting: bool = ..., tsl: bool = ..., unParent: bool = ..., up: bool = ..., unlockMainConnection: bool = ..., ulk: bool = ..., updateColorMode: bool = ..., ucm: bool = ..., updateMainConnection: bool = ..., upd: bool = ..., useBaseRenderer: bool = ..., ubr: bool = ..., useColorIndex: bool = ..., uci: bool = ..., useCustomBackground: bool = ..., ucb: bool = ..., useDefaultMaterial: bool = ..., udm: bool = ..., useInteractiveMode: bool = ..., ui: bool = ..., useRGBImagePlane: bool = ..., ip: bool = ..., useReducedRenderer: bool = ..., urr: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., userNode: Optional[Union[str, bool]] = ..., un: Optional[Union[str, bool]] = ..., viewColor: Optional[Union[Tuple[float, float, float, float], bool]] = ..., vc: Optional[Union[Tuple[float, float, float, float], bool]] = ..., viewObjects: bool = ..., vo: bool = ..., viewSelected: bool = ..., vs: bool = ..., viewType: bool = ..., vt: bool = ..., width: bool = ..., w: bool = ..., wireframeBackingStore: bool = ..., wbs: bool = ..., wireframeOnShaded: bool = ..., wos: bool = ..., xray: bool = ..., xr: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create, edit or query a model editor.
    
    Note that some of the flags of this command may have different settings
    for normal mode and for interactive/playback mode.  For example, a
    modelEditor can be set to use shaded mode normally, but to use wireframe
    during playback for greater speed.  Some flags also support having
    defaults set so that new model editors will be created with those settings.
    
    This is the main command for creating stereo editors. This commands
    only acts as an interface to the actual viewport. It is derived off of
    MPxModelEditorCommand. This command manages the set of stereo rig
    tools.

    Args:
        activeComponentsXray | acx: (edit, query) - Turns on or off Xray mode for active components.
        activeCustomEnvironment | ace: (edit) - Specifies a path to an image file to be used as environment map. It is only enabled when a valid scene render filter is specified.
        activeCustomGeometry | acg: (edit, query) - Specifies an identifier for custom geometry to override the geometry to display. It is only enabled when a valid scene render filter is specified.
        activeCustomLighSet | acl: (edit, query) - Specifies an identifier for the light set to use with a scene render filter. It is only enabled when a valid scene render filter is specified.
        activeCustomOverrideGeometry | aog: (edit, query) - Specifies an identifier for an override on the custom geometry for a scene render filter.
        activeCustomRenderer | acr: (edit, query) - Specifies an identifier for custom renderer to use when a valid scene render filter is also specified.
        activeOnly | ao: (edit, query) - Sets whether only active objects should appear shaded in shaded display.
        activeShadingGraph | asg: (edit, query) - Specifies the shading graph to use to override material display. Only enabled when a valid scene render filter is specified.
        activeSupported | ams: (query) - True if the viewer is capable of drawing in active mode which takes advantage of the graphics card's built-in stereoscopic support. This includes support for shutter glasses and stereo support in clone mode.
        activeView | av: (edit, query) - Sets this model editor to be the active view.  Returns true if successful.  On query this flag will return whether the view is the active view.
        addObjects | aob: (edit) - This flag causes the objects contained within the selection connection to be added to the list of objects visible in the view (if viewSelected is true).
        addSelected | addSelected: (edit) - This flag causes the currently active objects to be added to the list of objects visible in the view (if viewSelected is true).
        allObjects | alo: (edit, query) - Turn on/off the display of all objects for the view of the model editor. This excludes NURBS, CVs, hulls, grids and manipulators.
        backfaceCulling | bfc: (edit, query) - Turns on or off backface culling for the whole view.  This setting overrides the culling settings of individual objects.  All objects draw in the view will be backface culled.  When backface culling is turned on, surfaces becomes invisible in areas where the normal is pointing away from the camera.
        bluePencil | bp: (create, edit, query) - Define whether the blue pencil should be added or not
        bufferMode | bm: (edit, query) - Deprecated: this is not supported in Viewport 2.0.  Sets the graphic buffer mode.  Possible values are "single" or "double".
        bumpResolution | brz: (edit, query) - Set the resolution for "baked" bump map textures when using the hardware renderer. The default value is 512, 512 respectively.
        camera | cam: (edit, query) - Change or query the name of the camera in model editor.
        cameraName | cn: (create, edit) - Set the name of the panel's camera transform and shape. The shape name is computed by appending the string "Shape" to the transform name. This flag may not be queried.
        cameraSet | cst: (create, edit, query) - Name of the camera set
        cameraSetup | cs: (query) - Based on the model editor name passed in will returns a string list containing camera setups. A camera setup can contain one or more cameras which are associated with each other. Camera setups are defined as pairs of consecutive strings in the list. Each pair is comprised of: a string which identifies an active camera, and a string which defines a script to set up a given active camera. As many pairs of strings can be returned as the number of active cameras. If nothing is returned then it is assumed that no set up is required to activate a given camera.
        cameras | ca: (edit, query) - Turn on/off the display of cameras for the view of the model editor.
        capture | cpt: (edit, query) - Perform an one-time capture of the viewport to the named image file on disk.
        captureSequenceNumber | csn: (edit, query) - When a number greater or equal to 0 is specified each subsequent refresh will save an image file to disk if the capture flag has been enabled.  The naming of the file is:  {root name}.#.{extension}  if the name {root name}.{extension} is used for the capture flag argument.  The value of # starts at the number specified to for this argument and increments for each subsequent refresh.  Sequence capture can be disabled by specifying a number less than 0 or an empty file name for the capture flag.
        centerCamera | ccm: (query) - Only available in query mode: returns the current center camera of this view.
        colorMap | cm: (query) - Queries the color map style for the model panel. Possible values are "colorIndex" and "rgb".
        colorResolution | crz: (edit, query) - Set the resolution for "baked" color textures when using the hardware renderer. The default value is 256, 256 respectively.
        control | ctl: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        controlVertices | cv: (edit, query) - Turn on/off the display of NURBS CVs for the view of the model editor.
        cullingOverride | cov: (edit, query) - Set whether to override the culling attributes on objects when using the hardware renderer. The options are:  "none" : Use the culling object attributes per object. "doubleSided" : Force all objects to be double sided. "singleSided": Force all objects to be single sided.  The default value is "none".
        default | d: (edit, query) - Causes this command to modify the default value of this setting. Newly created model editors will inherit the values.  This flag may be used with the -interactive to set default interactive settings.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        deformers | df: (edit, query) - Turn on/off the display of deformer objects for the view of the model editor.
        dimensions | dim: (edit, query) - Turn on/off the display of dimension objects for the view of the model editor.
        displayAppearance | da: (edit, query) - Sets the display appearance of the model panel.  Possible values are "wireframe", "points", "boundingBox", "smoothShaded", "flatShaded".  This flag may be used with the -interactive and -default flags.  Note that only "wireframe", "points", and "boundingBox" are valid for the interactive mode.
        displayLights | dl: (edit, query) - Sets the lighting for shaded mode.  Possible values are "selected", "active", "all", "default", "none".
        displayMode | dm: (create, edit, query) - Defines the display mode for this view. Some modes are available only for certain types of graphics hardware. Valid values are:  active: uses the graphics card's built-in stereoscopic mode is available leftEye: displays only the view from the left camera. rightEye: displays only the view from the rigth camera. centerEye: displays only the view from the center camera. anaglyph: displays both left and right cameras, filtered using red and blue anaglyphLum: same as anaglyph, except the luminance is computed before the red and blue filtering interlace: displays an interlaced view of left and right cameras checkerboard: Same as interlace, except a checkerboard pattern is used to mix both images freeview: displays both left and right images, half size next to each other freeviewX: same as freeview, except left and right cameras are swapped
        displayTextures | dtx: (edit, query) - Turns on or off display of textures in shaded mode
        docTag | dtg: (create, edit, query) - Attaches a tag to the editor.
        dynamicConstraints | dc: (edit, query) - Turn on/off the display of dynamicConstraints for the view of the model editor.
        dynamics | dy: (edit, query) - Turn on/off the display of dynamics objects for the view of the model editor.
        editorChanged | ec: (create, edit, query) - An optional script callback which is called when the editors options have changed.  This is useful in a situation where a scripted panel contains a modelEditor and wants to be notified when the contained editor changes its options.
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter | f: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        filteredObjectList | fol: (query) - For model editors with filtering on (either using an object filter, or isolate select), this flag returns a string list of the objects which are displayed in this editor. Note that this list does not take into account visibility (based on camera frustum or flags), it purely captures the objects which are considered when rendering the view.
        fluids | fl: (edit, query) - Turn on/off the display of fluids for the view of the model editor.
        fogColor | fcl: (edit, query) - The color used for hardware fogging.
        fogDensity | fdn: (edit, query) - Determines the density of hardware fogging.
        fogEnd | fen: (edit, query) - The end location of hardware fogging.
        fogMode | fmd: (edit, query) - This determines the drop-off mode for fog. The possibilities are:  "linear" : linear drop-off "exponent" : exponential drop-off "exponent2" : squared exponential drop-off
        fogSource | fsc: (edit, query) - Set the type of fog algorithm to use. If the argument is "fragment" (default) then fog is computed per pixel. If the argument is "coordinate" then if the geometry has specified vertex fog coordinates, and the OpenGL extension for vertex fog is supported by the graphics system, then fog is computed per vertex.
        fogStart | fst: (edit, query) - The start location of hardware fogging.
        fogging | fg: (edit, query) - Set whether hardware fogging is enabled or not.
        follicles | fo: (edit, query) - Turn on/off the display of follicles for the view of the model editor.
        forceMainConnection | fmc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        grid | gr: (edit, query) - Turn on/off the display of the grid for the view of the model editor.
        hairSystems | hs: (edit, query) - Turn on/off the display of hairSystems for the view of the model editor.
        handles | ha: (edit, query) - Turn on/off the display of select handles for the view of the model editor.
        headsUpDisplay | hud: (edit, query) - Sets whether the model panel will draw any enabled heads up display	elements in this window (if true).  Currently this requires the HUD elements to be globally enabled.
        height | h: (query) - Return the height of the associated viewport in pixels
        highlightConnection | hlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        hulls | hu: (edit, query) - Turn on/off the display of NURBS hulls for the view of the model editor.
        ignorePanZoom | ipz: (edit, query) - Sets whether the model panel will ignore the 2D pan/zoom value to give an overview of the scene.
        ikHandles | ikh: (edit, query) - Turn on/off the display of ik handles and end effectors for the view of the model editor.
        imagePlane | imp: (edit, query) - Turn on/off the display of image plane for the view
        interactive | i: (edit, query) - Causes this command to modify the interactive refresh settings of the view.  In this way it is possible to change the behavior of the model editor during playback for improved performance.
        interactiveBackFaceCull | ibc: (create, edit, query) - Define whether interactive backface culling should be on or not
        interactiveDisableShadows | dis: (create, edit, query) - Define whether interactive shadows should be disabled or not
        isFiltered | isFiltered: (query) - Returns true for model editors with filtering applied to their view of the scene. This could either be an explicit object filter, or a display option such as isolate select which filters the objects that are displayed.
        jointXray | jx: (edit, query) - Turns on or off Xray mode for joints.
        joints | j: (edit, query) - Turn on/off the display of joints for the view of the model editor.
        leftCamera | lcm: (query) - Only available in query mode: returns the current left camera of this view.
        lights | lt: (edit, query) - Turn on/off the display of lights for the view of the model editor.
        lineWidth | lw: (edit, query) - Set width of lines for display
        locators | lc: (edit, query) - Turn on/off the display of locator objects for the view of the model editor.
        lockMainConnection | lck: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        lowQualityLighting | lql: (edit, query) - Set whether to use "low quality lighting" when using the hardware renderer. The default value is false.
        mainListConnection | mlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        manipulators | m: (edit, query) - Turn on/off the display of manipulator objects for the view of the model editor.
        maxConstantTransparency | mct: (edit, query) - Sets the maximum constant transparency.  Setting this value remaps constant transparency values from the range [0.0, 1.0] to the range [0.0, maxConstantTransparency]. All transparency values are shifted linearly to the new range, so a fully transparency object (transparency 1.0) would appear with a transparency of maxConstantTransparency in the viewport, allowing highly transparent objects to be made visible.  This flag only affects constant (non-textured) transparent objects.
        maximumNumHardwareLights | mhl: (create, edit, query) - Define whether the hardware light maximum should be respected or not
        modelPanel | mp: (create) - Allows the created model editor to be embedded in the named model panel. Intended for use with custom model editors created via the API (i.e. the flag would be used on the derived MPxModelEditorCommand), though the flag may also be used on the base modelEditor command to restore a default Maya model editor to the panel. Note that the model editor previously owned by the panel is deleted.
        motionTrails | mt: (edit, query) - Turn on/off the Motion Trail display in the Viewport.
        nCloths | ncl: (edit, query) - Turn on/off the display of nCloths for the view of the model editor.
        nParticles | npa: (edit, query) - Turn on/off the display of nParticles for the view of the model editor.
        nRigids | nr: (edit, query) - Turn on/off the display of nRigids for the view of the model editor.
        noUndo | nud: (edit) - This flag prevents some viewport operations (such as isolate select) from being added to the undo queue.
        nurbsCurves | nc: (edit, query) - Turn on/off the display of nurbs curves for the view of the model editor.
        nurbsSurfaces | ns: (edit, query) - Turn on/off the display of nurbs surfaces for the view of the model editor.
        objectFilter | obf: (edit, query) - Set or query the current object filter name. An object filter is required to have already been registered.
        objectFilterList | ofl: (query) - Return a list of names of registered filters.
        objectFilterListUI | ofu: (query) - Return a list of UI names of registered filters.
        objectFilterShowInHUD | ofs: (edit, query) - Sets whether or not to display the object filter UI name in the heads up display when an object filter is active. This string is concatenated with the camera name.
        objectFilterUI | obu: (query) - Query the current object filter UI name. The object filter is required to have already been registered.
        occlusionCulling | ocl: (edit, query) - Set whether to enable occlusion culling testing when using the hardware renderer. The default value is false.
        panel | pnl: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent | p: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        pivots | pv: (edit, query) - Turn on/off the display of transform pivots for the view of the model editor.
        planes | pl: (edit, query) - Turn on/off the display of sketch planes for the view of the model editor.
        pluginObjects | po: (edit, multiuse) - Turn on/off the display of plug-in objects for the view. It depends on the plug-in implementation whether to respect this flag.
        pluginShapes | ps: (edit) - Turn on/off the display of plug-in shapes for the view. It depends on the plug-in implementation whether to respect this flag.
        polymeshes | pm: (edit, query) - Turn on/off the display of polygon meshes for the view of the model editor.
        queryPluginObjects | qpo: (query) - Query the on/off state of plug-in objects display for the view. To set the on/off state, use -pluginObjects instead.
        removeSelected | rs: (edit) - This flag causes the currently active objects to be removed from the list of objects visible in the view (if viewSelected is true).
        rendererDeviceName | rdn: (query) - Query for the name of the draw API used by the Viewport 2.0 renderer for a 3d modeling viewport. The possible return values are "VirtualDeviceGL" if Maya is set to use "OpenGL - Legacy" for Viewport 2.0, "VirtualDeviceGLCore" if Maya is set to use "OpenGL - Core Profile" (either Compatibility or Strict) for Viewport 2.0, or "VirtualDeviceDx11" if Maya is set to use DirectX for Viewport 2.0. If the renderer for the 3d modeling viewport is not Viewport 2.0, an empty string will be returned.
        rendererList | rls: (query) - Query for a list of the internal names for renderers available for use with the 3d modeling viewport. The default list contains at least "vp2Renderer", if supported. See rendererName for more details on these renderers. Any plug-in viewport renderers will also appear in this list.
        rendererListUI | rlu: (query) - Query for a list of the UI names for renderers available for use with the 3d modeling viewport. The default list consists of the UI name for "vp2Renderer", if it is supported. Any plug-in viewport renderer's UI names will also appear in this list. This list and the list returned from rendererList have a 1:1 correspondance.
        rendererName | rnm: (edit, query) - Set or get the renderer used for a 3d modeling viewport. The name provided should be an internal name of a renderer. The 'rendererList' flag can be used to query for a list of available names. The default renderer is "vp2Renderer": Viewport 2.0.
        rendererOverrideList | rol: (query) - Query for a list of the internal names for renderer overrides for a 3d viewport renderer. Currently only the "Viewport 2" renderer supports renderer overrides.
        rendererOverrideListUI | rou: (query) - Query for a list of the UI names for renderer overrides for a 3d viewport renderer. Currently only the "Viewport 2" renderer supports renderer overrides.
        rendererOverrideName | rom: (edit, query) - Set or get the override used for a 3d viewport renderer. The name provided should be the internal name for an override.  The 'rendererOverrideList' flag can be used to query for a list of available names. Currently only the "Viewport 2" renderer  supports renderer overrides. Setting an empty string will unset any currently active override.
        resetCustomCamera | rcc: (edit) - When specified will reset the camera transform for the active custom camera used for a scene render filter. It is only enabled when a valid scene render filter is specified.
        rigRoot | rr: (create, edit, query) - Defines the rig root associated with this view.
        rightCamera | rcm: (query) - Only available in query mode: returns the current right camera of this view.
        sceneRenderFilter | srf: (edit, query) - Specifies the name of a scene render filter
        selectionConnection | slc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        selectionHiliteDisplay | sel: (edit, query) - Sets whether the model panel will draw any selection hiliting on the objects in this window.
        setSelected | ss: (edit) - This flag causes the currently active objects to be the only objects visible in the view (if viewSelected is true).
        shadingModel | sml: (create, edit, query) - Shading model to use
        shadows | sdw: (edit, query) - Turn on/off the display of hardware shadows in shaded mode.
        smallObjectCulling | soc: (create, edit, query) - Define whether small object culling should be enabled or not
        smallObjectThreshold | sot: (create, edit, query) - Threshold used for small object culling
        smoothWireframe | swf: (edit, query) - Turns on or off smoothing of wireframe lines and points
        sortTransparent | st: (edit, query) - This flag turns on/off sorting of transparent objects during shaded mode refresh. Normally, objects are sorted according to their origin in camera space but when this flag is turned off they will be drawn according to their (depth-first traversal) order in the scene graph. This is a global flag that affects all model editors.
        stateString | sts: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        stereoDrawMode | sdm: (create, edit, query) - If this flag is used then set stereo draw mode
        strokes | str: (edit, query) - Turn on/off the display of Paint Effects strokes for the view
        subdivSurfaces | sds: (edit, query) - Turn on/off the display of subdivision surfaces for the view of the model editor.
        swapEyes | se: (create, edit, query) - Swap the display of the left and right cameras. The left camera becomes the right draw pass and the right camera becomes the left draw pass. This flag is intended for advanced users, for situations where the hardware uses the opposite left/right convention.
        textureAnisotropic | ta: (edit, query) - Set whether to perform anisotropic texture filtering. Will work only if the anisotropic texture filtering extension is supported in OpenGL on the graphics system.
        textureCompression | tcp: (create, edit, query) - Defines whether texture compression should be used or not
        textureDisplay | td: (edit, query) - Set the type of blending to use for textures. The blend is performed between the destination fragment and the texture fragment. The source is usually the material color. Argument options are: "modulate" : multiply the destination and texture fragment "decal" : overwrite the destination with the texture fragment
        textureEnvironmentMap | tem: (create, edit, query) - If true then use a texture environment map
        textureHilight | th: (edit, query) - Set whether to show specular hilighting when the display is in shaded textured mode.
        textureMaxSize | tms: (edit, query) - Set maximum texture size for hardware texturing.  The integer value must be a power of 2.  Recommended values are 128 or 256.  If the value specified is larger than the OpenGL maximim textures size for the graphics hardware it will be clamped to the OpenGL size.  If many large textures are used in a scene reducing this value improves performance.  On Impact texture memory is pinned in RAM so using large textures can cause reliability and performance problems. Again reducing this value will help. Software rendering does not use this value. This flag is obsolete as of Maya 6.5. The maxTextureResolution/mtr argument on the displayPref command should be used instead.
        textureMemoryUsed | tmu: (query) - Returns the total number of bytes used by all texture maps.  This is typicly width*height*channels for all texture objects in the scene If the texture is mip mapped all mip map levels are included in the total though not never more than two level will be in use at one time
        textureSampling | ts: (edit, query) - Set the type of sampling to be used for texture display. The argument can be either:  1 : means to perform point sample 2 : means to perform bilinear interpolation (default)
        textures | tx: (edit, query) - Turn on/off the display of texture objects for the view
        transpInShadows | tis: (edit, query) - Set whether to enable display of transparency in shadows when using the hardware renderer. The default value is false.
        transparencyAlgorithm | tal: (edit, query) - Set the transparency algorithm. The options are:  1) "frontAndBackCull" : Two pass front and back culling technique. 2) "perPolygonSort" : Draw transparent polygons in back-to-front order technique.  transparency pptions 1) and 2) are supported by the hardware renderer. Options 1) is supported by the interactive modeling viewports. The default value is "frontAndBackCull".
        twoSidedLighting | tsl: (edit, query) - Turns on or off two sided lighting.  This may be used with the -default flag.
        unParent | up: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection | ulk: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateColorMode | ucm: (edit) - Using this flag tells the model panel to check which color mode it should be in, and to switch accordingly.  This flag may be used to update a model panel after a camera image plane has been added or removed.
        updateMainConnection | upd: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useBaseRenderer | ubr: (edit, query) - Set whether to use the "base" renderer when using the hardware renderer and in "interactive display mode" (-useInteractiveMode) The default value is false.
        useColorIndex | uci: (edit, query) - Sets whether the model panel will attempt to use color index mode when possible.  Color index mode can provide a performance increase for point, bounding box, and wireframe display modes. This may be used with the -default flag.
        useCustomBackground | ucb: (create, edit, query) - When set to true, instead of using the standard background, draw a solid background using the viewColor.
        useDefaultMaterial | udm: (edit, query) - Sets whether the model panel will draw all the shaded surfaces using the default material as opposed to using the material(s) currently assigned to the surfaces.
        useInteractiveMode | ui: (edit, query) - Turns on or off the use of the special interaction settings during playback.  This flag may be used with the -default flag.
        useRGBImagePlane | ip: (edit, query) - Sets whether the model panel will be forced into RGB mode when there is an image plane attached to the panel's camera.
        useReducedRenderer | urr: (create, edit, query) - Set true if using the reduced renderer
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        userNode | un: (edit, query) - Allows the user to associate a node name with the modelEditor. The value is automatically updated in the event the node is deleted or renamed.
        viewColor | vc: (create, edit, query) - Specifies the background color for the stereoscopic model editor. The default value is black which provides optimal stereoscopic viewing. This only applies if 'useCustomBackground' is on (which is the default).
        viewObjects | vo: (query) - Returns the name (if any) of the objectSet which contains the list of objects visible in the view if viewSelected is true and the list of objects being displayed does not come from the active list.
        viewSelected | vs: (edit, query) - This flag turns on/off viewing of selected objects. When the flag is set to true, the currently active objects are captured and used as the list of objects to view.
        viewType | vt: (query) - Returns a string indicating the type of the model editor. For the default model editor, returns the empty string. For custom model editor types created via the API, returns the same string as is returned via the method MPx3dModelView::viewType().
        width | w: (query) - Return the width of the associated viewport in pixels.
        wireframeBackingStore | wbs: (edit, query) - Sets whether a backing store is used to optimization the drawing of active objects. This mode can provide a performance increase in wireframe mode for certain scenes.
        wireframeOnShaded | wos: (edit, query) - Sets whether the model panel will draw the wireframe on all shaded objects (if true) or only for active objects (if false).
        xray | xr: (edit, query) - Turns on or off Xray mode.  This may be used with the -default flag.
    """
    ...


def stereoRigManager(*args, addRig: Optional[Union[Tuple[str, str, str], bool]] = ..., add: Optional[Union[Tuple[str, str, str], bool]] = ..., cameraSetFunc: Optional[Union[Tuple[str, str], bool]] = ..., csf: Optional[Union[Tuple[str, str], bool]] = ..., creationProcedure: Optional[Union[Tuple[str, str], bool]] = ..., cp: Optional[Union[Tuple[str, str], bool]] = ..., defaultRig: Optional[Union[str, bool]] = ..., dr: Optional[Union[str, bool]] = ..., delete: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., language: Optional[Union[Tuple[str, str], bool]] = ..., l: Optional[Union[Tuple[str, str], bool]] = ..., listRigs: bool = ..., lr: bool = ..., rigDefinition: Optional[Union[str, bool]] = ..., rd: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command manages the set of stereo rig tools.

    Args:
        addRig | add: (create) - Adds a new stereo rig definition. This flag takes 3 arguments: name, language, create:  name: A unique name for the rig type. lang: The language used for the callback. Valid values are "Python" and "MEL". Use the Python interface when possible. create: Procedure used to create a new rig of this type. This procedure takes no argument, and must return an array of strings. The first element is the root DAG node of the rig. The second and third elements are respectively the left and right cameras.
        cameraSetFunc | csf: (create) - Specifies the function to call when a rig is about to be added to a camera set. This function must be the same language as originally defined by the tool.
        creationProcedure | cp: (create) - Changes the creation procedure of an existing rig definition.  This flag takes 2 arguments: the name of the existing rig definition and the procedure.
        defaultRig | dr: (create, query) - Sets the default rig tool. The argument must be the name of one of the rigs added using the add flag.  Returns True if the default could be set, False otherwise.
        delete | d: (create) - Removes the definition of a stereo rig. The argument must be the name of one of the rigs added using the add flag.
        language | l: (create) - Changes the language of an existing rig definition. Valid values are "Python" and "MEL".  This flag takes 2 arguments: the name of the existing rig definition and the language keyword.
        listRigs | lr: (create) - When present, returns the list of all defined rigs. All other flags are ignored.
        rigDefinition | rd: (create) - Returns the definition of a rig, in the same format as the add flag. A string array containing lang, create cameraSet.  If an empty string is passed as the argument, then the default rig is used.
    """
    ...


def surfaceSampler(*args, camera: Optional[Union[str, bool]] = ..., cam: Optional[Union[str, bool]] = ..., fileFormat: Optional[Union[str, bool]] = ..., ff: Optional[Union[str, bool]] = ..., filename: Optional[Union[str, bool]] = ..., fn: Optional[Union[str, bool]] = ..., filterSize: Optional[Union[float, bool]] = ..., fs: Optional[Union[float, bool]] = ..., filterType: Optional[Union[int, bool]] = ..., ft: Optional[Union[int, bool]] = ..., flipU: bool = ..., fu: bool = ..., flipV: bool = ..., fv: bool = ..., ignoreMirroredFaces: bool = ..., imf: bool = ..., ignoreTransforms: bool = ..., it: bool = ..., mapHeight: Optional[Union[int, bool]] = ..., mh: Optional[Union[int, bool]] = ..., mapMaterials: bool = ..., mm: bool = ..., mapOutput: Optional[Union[str, bool]] = ..., mo: Optional[Union[str, bool]] = ..., mapSpace: Optional[Union[str, bool]] = ..., sp: Optional[Union[str, bool]] = ..., mapWidth: Optional[Union[int, bool]] = ..., mw: Optional[Union[int, bool]] = ..., maxSearchDistance: Optional[Union[float, bool]] = ..., msd: Optional[Union[float, bool]] = ..., maximumValue: Optional[Union[float, bool]] = ..., max: Optional[Union[float, bool]] = ..., overscan: Optional[Union[int, bool]] = ..., os: Optional[Union[int, bool]] = ..., searchCage: Optional[Union[str, bool]] = ..., sc: Optional[Union[str, bool]] = ..., searchMethod: Optional[Union[int, bool]] = ..., sm: Optional[Union[int, bool]] = ..., searchOffset: Optional[Union[float, bool]] = ..., so: Optional[Union[float, bool]] = ..., shadows: bool = ..., sh: bool = ..., source: Optional[Union[str, bool]] = ..., s: Optional[Union[str, bool]] = ..., sourceUVSpace: Optional[Union[str, bool]] = ..., sus: Optional[Union[str, bool]] = ..., superSampling: Optional[Union[int, bool]] = ..., ss: Optional[Union[int, bool]] = ..., target: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., targetUVSpace: Optional[Union[str, bool]] = ..., tus: Optional[Union[str, bool]] = ..., useGeometryNormals: bool = ..., ugn: bool = ..., uvSet: Optional[Union[str, bool]] = ..., uv: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Maps surface detail from a source surface to a new texture map on a target
    surface. Both objects must be selected when the command is invoked, with
    the source surface selected first, and the target last.

    Args:
        camera | cam: (create) - Specify the camera to use for camera specific lighting calculations such as specular highlights or reflections.
        fileFormat | ff: (create, multiuse) - The image format as a file extension (e.g. "dds"). This must be included once for every output map specified.
        filename | fn: (create, multiuse) - The filename to use when creating the map. This must be included once for every output map specified.
        filterSize | fs: (create) - The filter size to use in pixels. Larger values (e.g. over 2.0) will produce smoother/softer results, while values closer to 1.0 will produce sharper results.
        filterType | ft: (create) - The filter type to use. 0 is a Guassian filter, 1 is a triangular filter, 2 is a box filter.
        flipU | fu: (create) - Flip the U coordinate of the generated image.
        flipV | fv: (create) - Flip the V coordinate of the generated image.
        ignoreMirroredFaces | imf: (create) - Stops reverse wound (i.e. mirrored) faces from contributing to the map generation.
        ignoreTransforms | it: (create) - Controls whether transforms are used (meaning the search is performed in worldspace), or not (meaning the search is performed in object space).
        mapHeight | mh: (create, multiuse) - Pixel width of the generated map. This must be included once for every output map specified.
        mapMaterials | mm: (create, multiuse) - Where appropriate (e.g. normal maps), this controls whether the material should be included when sampling the map attribute. This must be included once for every output map specified.
        mapOutput | mo: (create, multiuse) - Specifies a new output map to create. One of "normal", "displacement" "diffuseRGB", "litAndShadedRGB", or "alpha"
        mapSpace | sp: (create, multiuse) - The space to generate the map in. Valid keyword is "object". Default is tangent space. This must be included once for every output map specified.
        mapWidth | mw: (create, multiuse) - Pixel width of the generated map. Some output image formats require even or power of 2. This must be included once for every output map specified.
        maxSearchDistance | msd: (create, multiuse) - Controls the maximum distance away from a target surface that will be searched for source surfaces. A value of 0 indicates no limit. When generated maps include artifacts from the "other side" of an object, try setting this value to a distance approximately equal to the radius of the object. If this flag is included, it must be included once for every target.
        maximumValue | max: (create, multiuse) - The maximum value to include in the map. This allows control of how floating point values (like displacement) are quantised into integer image formats.
        overscan | os: (create) - The number of additional pixels to render around UV borders. This will help to minimise texel filtering artifacts on UV seams. When mipmaps are going to be generated for the texture a higher value may be necessary (in addition to a filterSize greater than 1).
        searchCage | sc: (create, multiuse) - Specifies a search envelope surface to use as a search guide when looking for source surfaces. If this flag is included, it must be included once for every target.
        searchMethod | sm: (create) - Controls the search method used to match sample points on a target surface to points on the sources. 0 is closest to envelope, 1 is prefer any intersection inside envelope to intersections outside it, and 2 is only use intersections inside envelope.
        searchOffset | so: (create, multiuse) - Specifies a fixed offset from a target surface to use as the starting point when looking for source surfaces. This value is only used when no search cage is specified for a given target. If this flag is included, it must be included once for every target.
        shadows | sh: (create, multiuse) - Where appropriate (e.g. lit and shaded), this controls whether shadows are included in the calculation. Currently only depth map shadows are supported.
        source | s: (create, multiuse) - Specifies a surface to use as a sampling source
        sourceUVSpace | sus: (create, multiuse) - Specifies that the transfer of data between the surfaces should be done in UV space and specifies the name of the UV set on the source surface(s) that should be used as the transfer space.
        superSampling | ss: (create) - Controls the number of sampling points calculated for each output value. The algorithm will use 2 ^ n squared samples for each point (so a value of 0 will use a single sample, while a value of 3 will calculate 64 samples for each point).
        target | t: (create, multiuse) - Specified a surface to sample output information for.
        targetUVSpace | tus: (create, multiuse) - Specifies that the transfer of data between the surfaces should be done in UV space and specifies the name of the UV set on the target surface(s) that should be used as the transfer space.
        useGeometryNormals | ugn: (create) - Controls whether geometry or surface normals are used for surface searching. Using geometry normals will ensure a smooth mapping but can introduce distorted mappings where there are large distances between the source and target surfaces. Surface normals can introduce overlapping or discontinuous mappings, but does allow map distortion to be influenced by surface normal direction.
        uvSet | uv: (create, multiuse) - The name of the UV set to use when creating output maps. If this flag is included, it must be included once for every target.
    """
    ...


def surfaceShaderList(*args, add: Optional[Union[str, bool]] = ..., remove: Optional[Union[str, bool]] = ..., rm: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Add/Remove a relationship between an object and the
    current shading group.

    Args:
        add | add: (create) - add object(s) to shader group list.
        remove | rm: (create) - remove object(s) to shader group list.
    """
    ...


def swatchRefresh(*args) -> Any:
    r"""
    The swatchRefresh command causes image source node swatches to be
    refreshed on screen.  The purpose of this command is to provide a mechanism
    to trigger a swatch refresh in cases that are not subject to dirty propagation
    in the dependency graph.  This command only works with imageSource-derived
    node types. Invoking this command with no arguments will cause all imageSource
    swatches to be refreshed.

    Args:
    """
    ...


def textureWindow(*args, activeSelectionOnTop: bool = ..., ast: bool = ..., axesColor: Optional[Union[Tuple[float, float, float], bool]] = ..., axc: Optional[Union[Tuple[float, float, float], bool]] = ..., backFacingColor: Optional[Union[Tuple[float, float, float, float], bool]] = ..., bfc: Optional[Union[Tuple[float, float, float, float], bool]] = ..., capture: str = ..., cpt: str = ..., captureSequenceNumber: int = ..., csn: int = ..., changeCommand: Optional[Union[Tuple[str, str, str, str], bool]] = ..., cc: Optional[Union[Tuple[str, str, str, str], bool]] = ..., checkerColor1: Optional[Union[Tuple[float, float, float], bool]] = ..., cc1: Optional[Union[Tuple[float, float, float], bool]] = ..., checkerColor2: Optional[Union[Tuple[float, float, float], bool]] = ..., cc2: Optional[Union[Tuple[float, float, float], bool]] = ..., checkerColorMode: Optional[Union[int, bool]] = ..., ccm: Optional[Union[int, bool]] = ..., checkerDensity: Optional[Union[int, bool]] = ..., cd: Optional[Union[int, bool]] = ..., checkerDrawTileLabels: bool = ..., cdt: bool = ..., checkerGradient1: Optional[Union[Tuple[float, float, float], bool]] = ..., cg1: Optional[Union[Tuple[float, float, float], bool]] = ..., checkerGradient2: Optional[Union[Tuple[float, float, float], bool]] = ..., cg2: Optional[Union[Tuple[float, float, float], bool]] = ..., checkerGradientOverlay: bool = ..., cgo: bool = ..., checkerTileLabelColor: Optional[Union[Tuple[float, float, float], bool]] = ..., ctc: Optional[Union[Tuple[float, float, float], bool]] = ..., clearImage: bool = ..., ci: bool = ..., cmEnabled: bool = ..., cme: bool = ..., control: bool = ..., ctl: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., displayAxes: bool = ..., dax: bool = ..., displayCheckered: bool = ..., dct: bool = ..., displayDistortion: bool = ..., ddt: bool = ..., displayDivisionLines: bool = ..., ddl: bool = ..., displayGridLines: bool = ..., dgl: bool = ..., displayImage: Optional[Union[int, bool]] = ..., di: Optional[Union[int, bool]] = ..., displayIsolateSelectHUD: bool = ..., dih: bool = ..., displayLabels: bool = ..., dl: bool = ..., displayOverlappingUVCountHUD: bool = ..., doh: bool = ..., displayPreselection: bool = ..., dps: bool = ..., displayReversedUVCountHUD: bool = ..., drh: bool = ..., displaySolidMap: bool = ..., dsm: bool = ..., displayStyle: Optional[Union[str, bool]] = ..., dst: Optional[Union[str, bool]] = ..., displayTextureBorder: bool = ..., dtb: bool = ..., displayUVPositionHUD: bool = ..., duv: bool = ..., displayUVShellCountHUD: bool = ..., dsh: bool = ..., displayUVStatisticsHUD: bool = ..., duh: bool = ..., displayUsedPercentageHUD: bool = ..., dph: bool = ..., distortionAlpha: Optional[Union[float, bool]] = ..., dta: Optional[Union[float, bool]] = ..., distortionPerObject: bool = ..., dpo: bool = ..., divisions: Optional[Union[int, bool]] = ..., d: Optional[Union[int, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., doubleBuffer: bool = ..., dbf: bool = ..., drawAxis: bool = ..., da: bool = ..., drawSubregions: bool = ..., dsr: bool = ..., exists: bool = ..., ex: bool = ..., exposure: Optional[Union[float, bool]] = ..., exp: Optional[Union[float, bool]] = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., fmc: Optional[Union[str, bool]] = ..., forceRebake: bool = ..., frb: bool = ..., frameAll: bool = ..., fa: bool = ..., frameSelected: bool = ..., fs: bool = ..., frontFacingColor: Optional[Union[Tuple[float, float, float, float], bool]] = ..., ffc: Optional[Union[Tuple[float, float, float, float], bool]] = ..., gamma: Optional[Union[float, bool]] = ..., ga: Optional[Union[float, bool]] = ..., gridLinesColor: Optional[Union[Tuple[float, float, float], bool]] = ..., glc: Optional[Union[Tuple[float, float, float], bool]] = ..., gridNumbersColor: Optional[Union[Tuple[float, float, float], bool]] = ..., gnc: Optional[Union[Tuple[float, float, float], bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., hlc: Optional[Union[str, bool]] = ..., imageBaseColor: Optional[Union[Tuple[float, float, float], bool]] = ..., ibc: Optional[Union[Tuple[float, float, float], bool]] = ..., imageDim: bool = ..., idm: bool = ..., imageDisplay: bool = ..., id: bool = ..., imageNames: bool = ..., imn: bool = ..., imageNumber: Optional[Union[int, bool]] = ..., imagePixelSnap: bool = ..., ip: bool = ..., imageRatio: bool = ..., imr: bool = ..., imageRatioValue: Optional[Union[float, bool]] = ..., irv: Optional[Union[float, bool]] = ..., imageSize: bool = ..., imageTileRange: Optional[Union[Tuple[float, float, float, float], bool]] = ..., itr: Optional[Union[Tuple[float, float, float, float], bool]] = ..., imageUnfiltered: bool = ..., iuf: bool = ..., internalFaces: bool = ..., labelPosition: Optional[Union[str, bool]] = ..., lp: Optional[Union[str, bool]] = ..., loadImage: str = ..., li: str = ..., lockMainConnection: bool = ..., lck: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., mlc: Optional[Union[str, bool]] = ..., maxResolution: Optional[Union[int, bool]] = ..., mrs: Optional[Union[int, bool]] = ..., multiColorAlpha: Optional[Union[float, bool]] = ..., mca: Optional[Union[float, bool]] = ..., nbImages: bool = ..., nim: bool = ..., nextView: bool = ..., nv: bool = ..., numUvSets: bool = ..., nuv: bool = ..., numberOfImages: Optional[Union[int, bool]] = ..., ni: Optional[Union[int, bool]] = ..., numberOfTextures: Optional[Union[int, bool]] = ..., nt: Optional[Union[int, bool]] = ..., panel: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., previousView: bool = ..., pv: bool = ..., realSize: bool = ..., rs: bool = ..., refresh: bool = ..., ref: bool = ..., relatedFaces: bool = ..., rf: bool = ..., removeAllImages: bool = ..., ra: bool = ..., removeImage: bool = ..., ri: bool = ..., rendererString: Optional[Union[str, bool]] = ..., rds: Optional[Union[str, bool]] = ..., reset: bool = ..., r: bool = ..., saveImage: bool = ..., si: bool = ..., scaleBlue: Optional[Union[float, bool]] = ..., sb: Optional[Union[float, bool]] = ..., scaleGreen: Optional[Union[float, bool]] = ..., sg: Optional[Union[float, bool]] = ..., scaleRed: Optional[Union[float, bool]] = ..., sr: Optional[Union[float, bool]] = ..., selectInternalFaces: bool = ..., sif: bool = ..., selectRelatedFaces: bool = ..., srf: bool = ..., selectionConnection: Optional[Union[str, bool]] = ..., slc: Optional[Union[str, bool]] = ..., setUvSet: Optional[Union[int, bool]] = ..., suv: Optional[Union[int, bool]] = ..., singleBuffer: bool = ..., sbf: bool = ..., size: Optional[Union[float, bool]] = ..., s: Optional[Union[float, bool]] = ..., solidMap3dView: bool = ..., s3d: bool = ..., solidMapColorSeed: Optional[Union[int, bool]] = ..., scs: Optional[Union[int, bool]] = ..., solidMapPerShell: bool = ..., sps: bool = ..., spacing: Optional[Union[float, bool]] = ..., sp: Optional[Union[float, bool]] = ..., stateString: bool = ..., sts: bool = ..., style: Optional[Union[int, bool]] = ..., st: Optional[Union[int, bool]] = ..., subdivisionLinesColor: Optional[Union[Tuple[float, float, float], bool]] = ..., sdc: Optional[Union[Tuple[float, float, float], bool]] = ..., textureBorder3dView: bool = ..., t3d: bool = ..., textureBorderColor: Optional[Union[Tuple[float, float, float], bool]] = ..., tbc: Optional[Union[Tuple[float, float, float], bool]] = ..., textureBorderWidth: Optional[Union[int, bool]] = ..., tbw: Optional[Union[int, bool]] = ..., textureNames: bool = ..., txn: bool = ..., textureNumber: Optional[Union[int, bool]] = ..., tn: Optional[Union[int, bool]] = ..., tileLabels: bool = ..., tlb: bool = ..., tileLinesColor: Optional[Union[Tuple[float, float, float], bool]] = ..., tlc: Optional[Union[Tuple[float, float, float], bool]] = ..., toggle: bool = ..., tgl: bool = ..., toggleExposure: bool = ..., tge: bool = ..., toggleGamma: bool = ..., tgg: bool = ..., unParent: bool = ..., up: bool = ..., unlockMainConnection: bool = ..., ulk: bool = ..., updateMainConnection: bool = ..., upd: bool = ..., useFaceGroup: bool = ..., uf: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., usedPercentageHUDRange: Optional[Union[Tuple[float, float, float, float], bool]] = ..., upr: Optional[Union[Tuple[float, float, float, float], bool]] = ..., uvSets: bool = ..., uvs: bool = ..., viewPortImage: bool = ..., vpi: bool = ..., viewTransformName: Optional[Union[str, bool]] = ..., vtn: Optional[Union[str, bool]] = ..., wireframeComponentColor: Optional[Union[Tuple[float, float, float, float], bool]] = ..., wcc: Optional[Union[Tuple[float, float, float, float], bool]] = ..., wireframeObjectColor: Optional[Union[Tuple[float, float, float, float], bool]] = ..., woc: Optional[Union[Tuple[float, float, float, float], bool]] = ..., writeImage: str = ..., wi: str = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create a UV Editor and to query or edit
    the texture editor settings.
    
    The UV Editor displays texture mapped polygon objects in 2D
    texture space. Only active objects are visible in this window.
    
    The UV Editor has the ability to display two types of images. The
    Texture Image is a visualisation of the current texture and associated
    placement parameters. The Editor Image is a user specified image loaded
    from disk.
    
    A UV Editor can be invoked by selecting the "Window -> UV
    Texture Editor..." menu item from the main maya menu listing that
    appears at the top of the maya window. It can also be invoked by
    selecting the "Panel -> UV Editor" item under the "Panels"
    menu item that appears at the top right hand corner of the view.
    
    As a UV Editor typically exists at start-up time, and as only
    one of these can exist at any given time, this command is normally
    used to query and edit the editor settings.

    Args:
        activeSelectionOnTop | ast: (create, edit, query) - Display the solid map / distortion of active selection on top of others.
        axesColor | axc: (create, edit, query) - The color of axes, default is 0.0 0.0 1.0
        backFacingColor | bfc: (create, edit, query) - Sets or queries the RGBA back facing color.
        capture | cpt: (edit) - Perform an one-time capture of the viewport to the named image file on disk.
        captureSequenceNumber | csn: (edit) - When a number greater or equal to 0 is specified each subsequent refresh will save an image file to disk if the capture flag has been enabled.  The naming of the file is:  {root name}.#.{extension}  if the name {root name}.{extension} is used for the capture flag argument. The value of # starts at the number specified to for this argument and increments for each subsequent refresh.  Sequence capture can be disabled by specifying a number less than 0 or an empty file name for the capture flag.
        changeCommand | cc: (create, edit, query) - Parameters:  First string: command Second string: editorName Third string: editorCmd Fourth string: updateFunc   Call the command when something changes in the editor The command should have this prototype :  command(string $editor, string $editorCmd, string $updateFunc, int $reason)  The possible reasons could be :  0: no particular reason 1: scale color 2: buffer (single/double) 3: axis  4: image displayed 5: image saved in memory
        checkerColor1 | cc1: (create, edit, query) - Sets the first color of the checker and identification pattern, when color mode is 2-colors.
        checkerColor2 | cc2: (create, edit, query) - Sets the second color of the checker and identification pattern, when color mode is 2-colors.
        checkerColorMode | ccm: (create, edit, query) - Sets the color mode of the checker and identification pattern. 0: multi-colors; 1: 2-colors;
        checkerDensity | cd: (create, edit, query) - Sets the density of the checker and identification pattern.
        checkerDrawTileLabels | cdt: (create, edit, query) - Toggles the checker tile label display.
        checkerGradient1 | cg1: (create, edit, query) - Sets the first gradient of the checker and identification pattern, when color mode is 2-colors.
        checkerGradient2 | cg2: (create, edit, query) - Sets the second gradient of the checker and identification pattern, when color mode is 2-colors.
        checkerGradientOverlay | cgo: (create, edit, query) - Toggle application of the gradient.
        checkerTileLabelColor | ctc: (create, edit, query) - Sets the checker tile label color.
        clearImage | ci: (edit) - Clears the current Editor Image.
        cmEnabled | cme: (edit, query) - Turn on or off applying color management in the editor.  If set, the color management configuration set in the current editor is used.
        control | ctl: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        displayAxes | dax: (edit, query) - Specify true to display the grid axes.
        displayCheckered | dct: (create, edit, query) - Display a unique checker and identification pattern for each UV tiles.
        displayDistortion | ddt: (create, edit, query) - Display the layout in shaded colors to indentify areas with stretched/squashed UVs
        displayDivisionLines | ddl: (edit, query) - Specify true to display the subdivision lines between grid lines.
        displayGridLines | dgl: (edit, query) - Specify true to display the grid lines.
        displayImage | di: (edit, query) - Set a particular image in the Editor Image Stack as the current Editor Image. Images are added to the Editor Image Stack using the "si/saveImage" flag.
        displayIsolateSelectHUD | dih: (create, edit, query) - Show heads-up display of isolate selection
        displayLabels | dl: (edit, query) - Specify true to display the grid line numeric labels.
        displayOverlappingUVCountHUD | doh: (create, edit, query) - Show heads-up display of overlapping UV count, as a part UV Statistics HUD
        displayPreselection | dps: (create, edit, query) - Toggles the pre-selection display.
        displayReversedUVCountHUD | drh: (create, edit, query) - Show heads-up display of UV Shells, as a part UV Statistics HUD
        displaySolidMap | dsm: (create, edit, query) - Display a solid overlay for the active texture map.
        displayStyle | dst: (create, edit, query) - Set the mode to display the image. Valid values are:  "color" to display the basic RGB image "mask" to display the mask channel "lum" to display the luminance of the image
        displayTextureBorder | dtb: (create, edit, query) - Toggles the texture borders display.
        displayUVPositionHUD | duv: (create, edit, query) - Show heads-up display of UV positions
        displayUVShellCountHUD | dsh: (create, edit, query) - Show heads-up display of UV Shell count, as a part UV Statistics HUD
        displayUVStatisticsHUD | duh: (create, edit, query) - Show heads-up display of UV Statistics
        displayUsedPercentageHUD | dph: (create, edit, query) - Show heads-up display of used UV space percentage, as a part UV Statistics HUD
        distortionAlpha | dta: (create, edit, query) - Set or query the distortion display alpha.
        distortionPerObject | dpo: (create, edit, query) - Toggles the per-object distortion display.
        divisions | d: (create, edit, query) - Sets the number of subdivisions between main grid lines.
        docTag | dtg: (create, edit, query) - Attaches a tag to the editor.
        doubleBuffer | dbf: (create, edit, query) - Set the display in double buffer mode
        drawAxis | da: (create, edit, query) - Set or query whether the axis will be drawn.
        drawSubregions | dsr: (create, edit, query) - Toggles the subregion display.
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        exposure | exp: (edit, query) - The exposure value used by the color management of the current editor.
        filter | f: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection | fmc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        forceRebake | frb: (create, edit) - Forces the current cache texture to refresh.
        frameAll | fa: (create) - This will zoom on the whole scene.
        frameSelected | fs: (create) - This will zoom on the currently selected objects.
        frontFacingColor | ffc: (create, edit, query) - Sets or queries the RGBA front facing color.
        gamma | ga: (edit, query) - The gamma value used by the color management of the current editor.
        gridLinesColor | glc: (create, edit, query) - The color of grid lines, default is 0.325 0.325 0.325
        gridNumbersColor | gnc: (create, edit, query) - The color of grid numbers, default is 0.2 0.2 0.2
        highlightConnection | hlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        imageBaseColor | ibc: (create, edit, query) - The base color of the image, default is white 1.0 1.0 1.0
        imageDim | idm: (create, edit, query) - Toggles the image dimming.
        imageDisplay | id: (edit, query) - Toggles the Texture Image display.
        imageNames | imn: (query) - List image names for all Texture Images available for display, if any.
        imageNumber | imageNumber: (edit, query) - Sets the number of Texture Images to display. This depends on the number of textures corresponding to the current selection. If there are N textures, then the possible Texture Image numbers are 0 to N-1.
        imagePixelSnap | ip: (edit, query) - Sets a mode so that UV transformations in the UV Texture Editor will cause UV values to snap to image pixel corners. Which pixels are used depends on whether a Texture Image or an Editor Image is being displayed. If both are displayed, the Texture Image pixels will be used.
        imageRatio | imr: (edit, query) - Sets the window to draw using the Texture Image's height versus width ratio. If the width is greater than the height, then the width is set to be 1 "unit" in the window, and the height is adjusted by width divided by height. This only affects the display of a Texture Image, not an Editor Image.
        imageRatioValue | irv: (query) - Query current image ratio value in UV Editor.
        imageSize | imageSize: (query) - Returns the size of the Texture Image currently being displayed. The values returned are width followed by height. Image size can only be queried.
        imageTileRange | itr: (edit, query) - Sets the UV range of the display. The 4 values specify the minimum U, V and maximum U, V in that order. When viewing a texture image, these values affect how many times the image is tiled based on appropriate parameters (e.g. Repeat UV, Mirror, Wrap, etc...) When viewing an Editor Image these values determine the visible size of the image. For example, setting the range to ( 0, 0, 2, 1 ) will cause the Editor Image to be loaded into a 2x1 rectangle, distorting it as necessary to fill the available space.
        imageUnfiltered | iuf: (edit, query) - Sets the Texture Image to draw unfiltered. The image will appear "pixelated" when the display resolution is higher than the resolution of the image.
        internalFaces | internalFaces: (create, edit, query) - Display contained faces by the selected components.
        labelPosition | lp: (edit, query) - The position of the grid's numeric labels. Valid values are "axis" and "edge".
        loadImage | li: (edit) - load an image from disk and set it as the current Editor Image
        lockMainConnection | lck: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        mainListConnection | mlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        maxResolution | mrs: (create, edit, query) - This flag will set the current cached texture's maximum resolution.
        multiColorAlpha | mca: (create, edit, query) - Sets the multi-color alpha of shaded UVs.
        nbImages | nim: (query) - returns the number of images
        nextView | nv: (edit) - Switches to the next view.
        numUvSets | nuv: (create, edit, query) - This flag will return the number of UV sets for selected objects in the texture window.
        numberOfImages | ni: (query) - The number of Texture Images currently available. for display.
        numberOfTextures | nt: (query) - The number of textures currently available. for display.
        panel | pnl: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent | p: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        previousView | pv: (edit) - Switches to the previous view.
        realSize | rs: (create) - This will display the image with the size of the internal buffer. Note: This argument no long has any affect on image display.
        refresh | ref: (edit) - requests a refresh of the current Editor Image.
        relatedFaces | rf: (create, edit, query) - Display connected faces by the selected components.
        removeAllImages | ra: (edit) - remove all the Editor Images from the Editor Image Stack
        removeImage | ri: (edit) - remove the current Editor Image from the Editor Image Stack
        rendererString | rds: (create, edit, query) - Set or query the string describing the current renderer.
        reset | r: (create) - Resets the ground plane to its default values.
        saveImage | si: (edit) - save the current Editor Image to memory. Saved Editor Images are stored in an Editor Image Stack. The most recently saved image is stored in position 0, the second most recently saved image in position 1, and so on... To set the current Editor Image to a previously saved image use the "di/displayImage" flag.
        scaleBlue | sb: (create, edit, query) - Define the scaling factor for the blue component in the View. The default value is 1 and can be between -1000 to +1000
        scaleGreen | sg: (create, edit, query) - Define the scaling factor for the green component in the View. The default value is 1 and can be between -1000 to +1000
        scaleRed | sr: (create, edit, query) - Define the scaling factor for the red component in the View. The default value is 1 and can be between -1000 to +1000
        selectInternalFaces | sif: (create, edit, query) - Add to selectionList the faces which are contained by (internal to) selected components.
        selectRelatedFaces | srf: (create) - Add to selectionList the faces which are connected to (non-internally related to) selected components.
        selectionConnection | slc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        setUvSet | suv: (create, edit) - This flag will set the current UV set on one given selected object within the texture window.
        singleBuffer | sbf: (create, edit, query) - Set the display in single buffer mode
        size | s: (create, edit, query) - Sets the size of the grid.
        solidMap3dView | s3d: (create, edit, query) - Display a solid overlay for the active texture map in 3D viewport.
        solidMapColorSeed | scs: (create, edit, query) - Sets the multi-color seed of shaded UVs.
        solidMapPerShell | sps: (create, edit, query) - Display a solid overlay with a random color per shell.
        spacing | sp: (create) - Sets the spacing between main grid lines.
        stateString | sts: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        style | st: (edit, query) - This flag is obsolete and should not be used.
        subdivisionLinesColor | sdc: (create, edit, query) - The color of subdivision lines, default is 0.25 0.25 0.25
        textureBorder3dView | t3d: (create, edit, query) - Toggles the texture borders display in 3d viewport.
        textureBorderColor | tbc: (create, edit, query) - Sets the display color of texture border.
        textureBorderWidth | tbw: (create, edit, query) - Set the display edge width of texture border.
        textureNames | txn: (query) - Texture names for all Texture Images available for display, if any.
        textureNumber | tn: (edit, query) - Sets the number of textures to display This depends on the number of textures corresponding to the current selection. If there are N textures, then the possible Texture Image numbers are 0 to N-1.
        tileLabels | tlb: (create, edit, query) - Toggles the texture tile label display.
        tileLinesColor | tlc: (create, edit, query) - The color of tile lines, default is 0.0 0.0 0.0
        toggle | tgl: (create, edit, query) - Toggles the ground plane display.
        toggleExposure | tge: (edit) - Toggles between the current and the default exposure value of the editor.
        toggleGamma | tgg: (edit) - Toggles between the current and the default gamma value of the editor.
        unParent | up: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection | ulk: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection | upd: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useFaceGroup | uf: (create, edit, query) - Display faces that are associated with the groupId that is set on the mesh node that is drawn. (The attribute "displayFacesWithGroupId")
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        usedPercentageHUDRange | upr: (create, edit, query) - Sets the range when calculating used UV space percentage. The 4 values specify the minimum U, V and maximum U, V in that order., default is 0 0 1 1.
        uvSets | uvs: (create, edit, query) - This flag will return strings containing UV set and object name pairs for selected objects in the texture window. The syntax of each pair is "objectName | uvSetName", where | is a literal character.
        viewPortImage | vpi: (create, edit) - Toggles the view port/ caching Texture Images.
        viewTransformName | vtn: (edit, query) - Sets the view pipeline to be applied if color management is enabled in the current editor.
        wireframeComponentColor | wcc: (create, edit, query) - Sets or queries the RGBA component wireframe color.
        wireframeObjectColor | woc: (create, edit, query) - Sets or queries the RGBA object wireframe color.
        writeImage | wi: (edit) - write the current Editor Image to disk
    """
    ...


def track(*args, down: Optional[Union[float, bool]] = ..., d: Optional[Union[float, bool]] = ..., left: Optional[Union[float, bool]] = ..., l: Optional[Union[float, bool]] = ..., right: Optional[Union[float, bool]] = ..., r: Optional[Union[float, bool]] = ..., upDistance01: Optional[Union[float, bool]] = ..., u: Optional[Union[float, bool]] = ..., upDistance02: Optional[Union[float, bool]] = ..., up: Optional[Union[float, bool]] = ...) -> Any:
    r"""
    The track command translates a camera horizontally or vertically
    in the world space. The viewing-direction and up-direction of the
    camera are not altered. There is no translation in the viewing
    direction.
    
    The track command can be applied to either a perspective or an
    orthographic camera.
    
    When no camera name is supplied, this command is applied to the
    camera in the active view.

    Args:
        down | d: (create) - Set the amount of down translation in unit distance.
        left | l: (create) - Set the amount of left translation in unit distance.
        right | r: (create) - Set the amount of right translation in unit distance.
        upDistance01 | u: (create) - Set the amount of up translation in unit distance. This is equivalent to using up/upDistance02 flag.
        upDistance02 | up: (create) - Set the amount of up translation in unit distance. This is equivalent to using u/upDistance01 flag.
    """
    ...


def tumble(*args, azimuthAngle: Optional[Union[float, bool]] = ..., aa: Optional[Union[float, bool]] = ..., elevationAngle: Optional[Union[float, bool]] = ..., ea: Optional[Union[float, bool]] = ..., localTumble: Optional[Union[int, bool]] = ..., lt: Optional[Union[int, bool]] = ..., pivotPoint: Optional[Union[Tuple[float, float, float], bool]] = ..., pp: Optional[Union[Tuple[float, float, float], bool]] = ..., rotationAngles: Optional[Union[Tuple[float, float], bool]] = ..., ra: Optional[Union[Tuple[float, float], bool]] = ...) -> Any:
    r"""
    The tumble command revolves the camera(s) by varying the azimuth
    and elevation angles in the perspective window. When both the
    azimuth and the elevation angles are supplied on the command line,
    the camera is firstly tumbled for the azimuth angle, then tumbled
    for the elevation angle. 
    
    When no camera name is supplied, this command is applied to the
    camera in the active view. 
    
    The camera's rotate pivot will override a specified pivot point if
    the rotate pivot is not at the camera's eye point.

    Args:
        azimuthAngle | aa: (create) - Degrees to change the azimuth angle.
        elevationAngle | ea: (create) - Degrees to change the elevation angle.
        localTumble | lt: (create) - Describes what point the camera will tumble around: 0 for the camera's tumble pivot, 1 for the camera's center of interest, and 2 for the camera's local axis, offset by its tumble pivot.
        pivotPoint | pp: (create) - Three dimensional point used as the pivot point in the world space.
        rotationAngles | ra: (create) - Two values in degrees to change the azimuth and elevation angles.
    """
    ...


def uvLink(*args, b: bool = ..., isValid: bool = ..., iv: bool = ..., make: bool = ..., m: bool = ..., queryObject: Optional[Union[str, bool]] = ..., qo: Optional[Union[str, bool]] = ..., texture: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., uvSet: Optional[Union[str, bool]] = ..., uvs: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command is used to make, break and query UV linking
    relationships between UV sets on objects and textures that use those
    UV sets.
    
    If no make, break or query flag is specified and both uvSet and
    texture flags are present, the make flag is assumed to be specified.
    
    If no make, break or query flag is specified and only one of the
    uvSet and texture flags is present, the query flag is assumed to be
    specified.
    
    The term "texture" in the context of UV linking is a bit of an
    oversimplification. In fact, UV sets can be linked to any node which
    takes UV coordinates as input. However in most cases it will be a
    texture to which you wish to link a UV set.

    Args:
        b | b: (create) - The presence of this flag on the command indicates that the command is being invoked to break links between UV sets and textures.
        isValid | iv: (create) - This flag is used to verify whether or not a texture or UV set is valid for the purposes of UV linking. It should be used in conjunction with either the -texture flag or the -uvSet flag, but not both at the same time.
        make | m: (create) - The presence of this flag on the command indicates that the command is being invoked to make links between UV sets and textures.
        queryObject | qo: (create) - This flag should only be used in conjunction with a query of a texture. This flag is used to indicate that the results of the query should be limited to UV sets of the object specified by this flag.
        texture | t: (create) - The argument to the texture flag specifies the texture to be used by the command in performing the action.
        uvSet | uvs: (create) - The argument to the uvSet flag specifies the UV set to be used by the command in performing the action.
    """
    ...


def vectorize(*args, browserView: bool = ..., bv: bool = ..., byFrame: Optional[Union[float, bool]] = ..., bf: Optional[Union[float, bool]] = ..., camera: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., combineFillsEdges: bool = ..., cfe: bool = ..., currentFrame: bool = ..., cf: bool = ..., curveTolerance: Optional[Union[float, bool]] = ..., ct: Optional[Union[float, bool]] = ..., customExtension: Optional[Union[str, bool]] = ..., ce: Optional[Union[str, bool]] = ..., detailLevel: Optional[Union[int, bool]] = ..., dl: Optional[Union[int, bool]] = ..., edgeColor: Optional[Union[Tuple[int, int, int], bool]] = ..., ec: Optional[Union[Tuple[int, int, int], bool]] = ..., edgeDetail: bool = ..., ed: bool = ..., edgeStyle: Optional[Union[str, bool]] = ..., es: Optional[Union[str, bool]] = ..., edgeWeight: Optional[Union[float, bool]] = ..., ew: Optional[Union[float, bool]] = ..., endFrame: Optional[Union[float, bool]] = ..., ef: Optional[Union[float, bool]] = ..., filenameFormat: Optional[Union[str, bool]] = ..., ff: Optional[Union[str, bool]] = ..., fillStyle: Optional[Union[str, bool]] = ..., fs: Optional[Union[str, bool]] = ..., flashVersion: Optional[Union[int, bool]] = ..., fv: Optional[Union[int, bool]] = ..., frameRate: Optional[Union[int, bool]] = ..., fr: Optional[Union[int, bool]] = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., hiddenEdges: bool = ..., he: bool = ..., highlightLevel: Optional[Union[int, bool]] = ..., hl: Optional[Union[int, bool]] = ..., highlights: bool = ..., hi: bool = ..., imageFormat: Optional[Union[str, bool]] = ..., layer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., minEdgeAngle: Optional[Union[float, bool]] = ..., mea: Optional[Union[float, bool]] = ..., outlinesAtIntersections: bool = ..., oai: bool = ..., outputFileName: Optional[Union[str, bool]] = ..., of: Optional[Union[str, bool]] = ..., pixelAspectRatio: Optional[Union[float, bool]] = ..., par: Optional[Union[float, bool]] = ..., reflectionDepth: Optional[Union[int, bool]] = ..., rd: Optional[Union[int, bool]] = ..., reflections: bool = ..., rf: bool = ..., renderLayers: bool = ..., rl: bool = ..., renderOptimization: Optional[Union[str, bool]] = ..., ro: Optional[Union[str, bool]] = ..., renderView: bool = ..., rv: bool = ..., secondaryCurveFitting: bool = ..., scf: bool = ..., shadows: bool = ..., sh: bool = ..., showBackFaces: bool = ..., sb: bool = ..., startFrame: Optional[Union[float, bool]] = ..., sf: Optional[Union[float, bool]] = ..., svgAnimation: Optional[Union[str, bool]] = ..., sa: Optional[Union[str, bool]] = ..., svgCompression: bool = ..., sc: bool = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    This command renders Maya scenes to various vector and raster formats
    using the Maya Vector renderer.

    Args:
        browserView | bv: (create) - Specifies whether to preview the render in the browser.  This option is swf only.
        byFrame | bf: (create) - Specifies the frame increment.
        camera | c: (create) - Specifies the camera to render.
        combineFillsEdges | cfe: (create) - Specifies whether fills and edges should be combined as a single object in Flash. This option is swf only.
        currentFrame | cf: (create) - Specifies whether to render the current frame only.
        curveTolerance | ct: (create) - Specifies the curve tolerance.  Valid values are in the range: 0.0 to 15.0.  The curve tolerance determines how aggressively the renderer tries to fit a series of connected, consecutive line segments to a curve. A value of 0.0 causes all line segments to be drawn without curve fitting.  A value of 15.0 causes aggressive curve fitting.
        customExtension | ce: (create) - Specifies a custom extension to use for the filename. Any non-empty string is valid.
        detailLevel | dl: (create) - Specifies the detail level.  Valid values are:  0 to 50.  The smaller the value, the more polygons may be combined to produce smaller files.  A higher value results in a more accurate render, but also larger files and longer render times.
        edgeColor | ec: (create) - Specifies the red, green, and blue components of the edge color.  Valid values are: 0 to 255 for each color component.
        edgeDetail | ed: (create) - Specifies whether edge detail should be rendered; ie. edges that have an angle between the face normals of any two adjacent polygons sharing an edge that is greater than the minimum edge angle (specified by the -mea flag).
        edgeStyle | es: (create) - Specifies the edge style.  Valid values are:  "Outline", "EntireMesh", "None".
        edgeWeight | ew: (create) - Specifies the edge weight to be used for all edges in points.  There are 72 points per inch.  A value of 0.0 specifies hairline edge weight.
        endFrame | ef: (create) - Specifies the end frame.
        filenameFormat | ff: (create) - Specifies the file name format.  Valid values are:  "name", "name.ext", "name.#.ext", "name.ext.#", "name.#", "name#.ext", "name_#.ext".
        fillStyle | fs: (create) - Specifies the fill style.  Valid values are:  "SingleColor", "TwoColor", "FourColor", "FullColor", "AverageColor", "AreaGradient", "MeshGradient", "None".  AreaGradient and MeshGradient are not available for the eps and ai image formats.
        flashVersion | fv: (create) - Specifies the Flash version of the swf output.  Valid values are:  3, 4, 5.  This option is swf only.
        frameRate | fr: (create) - Specifies the frame rate.  This option is for svg and swf only.
        height | h: (create) - Specifies the height of the output image in pixels.
        hiddenEdges | he: (create) - Specifies whether hidden edges should be rendered; ie. edges that have are not visible from the camera.
        highlightLevel | hl: (create) - Specifies the highlight level.  Valid values are:  1 to 8.  The value specifies how many concentric rings will be used to render an object's highlight.  This option is for the SingleColor, AverageColor, and AreaGradient fill styles only.
        highlights | hi: (create) - Specifies whether highlights should be rendered.  This option has no effect for ai, eps, and svg.  This option is for the SingleColor, AverageColor, and AreaGradient fill styles only.
        imageFormat | imageFormat: (create) - Specifies the image format to render. Valid values for the Windows and Mac platforms are: "swf", "eps", "ai", "svg", "jpg", "iff", "sgi", "tga", "tif", "bmp". Additional valid values for the Windows platform are: "als", "cin", "gif", "yuv", "rla", "si".  Additional valid values for the Mac platform are: "pntg", "ps", "png", "pict", "qtif", "qt".
        layer | l: (create) - Render the specified render layer.         Only this render layer will be rendered,         regardless of the renderable attribute value of the render layer.         The layer name will be appended to the output image file name.         The specified render layer becomes the current render layer before rendering,         and remains as current render layer after the rendering.
        minEdgeAngle | mea: (create) - Specifies the minimum edge angle in degrees.  Valid values are: 0.0 to 90.0.  This angle is the minimum angle between adjacent polygon face normals that is used to determine if the edge is rendered when the -ed flag is specified.
        outlinesAtIntersections | oai: (create) - Specifies if edges should be drawn when two polygons intersect. By default this flag is enabled.
        outputFileName | of: (create) - Specifies the output file name.
        pixelAspectRatio | par: (create) - Specifes the pixel aspect ratio.
        reflectionDepth | rd: (create) - Specifies the reflection depth.  Valid values are:  1 to 4.  The value specifies how many levels of reflection will be applied.  This option has no effect for ai, eps, and svg.
        reflections | rf: (create) - Specifies whether reflections should be rendered.  This option has no effect for ai, eps, and svg.
        renderLayers | rl: (create) - Specifies whether render layers should be rendered into separate files.
        renderOptimization | ro: (create) - Specifies the render optimization. Valid values are:  "Safe", "Good", "Aggressive". "Safe"  will  remove redundant geometry. "Good" removes redundant geometry as well as sub-pixel geometry that would not be visible without zooming into the high detail area. "Agressive" removes all of the geometry that "Good" removes but will also remove geometry at slightly above the single pixel level making it possible to visibly detect the removed geometry without zooming in on the affected region.
        renderView | rv: (create) - Specifies whether to display the rendered image to the render view.  This option is not applicable when batch rendering.
        secondaryCurveFitting | scf: (create) - Specifies whether to do secondary curve fitting.
        shadows | sh: (create) - Specifies whether shadows should be rendered.  This option has no effect for ai, eps, and svg.
        showBackFaces | sb: (create) - Specifies whether back faces will should be rendered; ie. faces whose normals are pointed away from the camera.
        startFrame | sf: (create) - Specifies the start frame.
        svgAnimation | sa: (create) - Specifies the SVG animation type.  Valid values are:  "Native", "HTMLScript".  This option is SVG only.
        svgCompression | sc: (create) - Specifies whether the SVG output should be compressed.  This option is svg only.
        width | w: (create) - Specifies the width of the output image in pixels.
    """
    ...


def viewCamera(*args, move: Optional[Union[str, bool]] = ..., m: Optional[Union[str, bool]] = ..., sideView: bool = ..., s: bool = ..., topView: bool = ..., t: bool = ...) -> Any:
    r"""
    The viewCamera command is used to position a camera to look
    directly at the side or top of another camera. This is primarily
    useful for the user when he or she is setting depth-of-field and
    clipping planes, if they are being used.
    
    The default behaviour: If no other flags are specified, the camera
    in the active panel is moved and the -t is presumed. If there is a
    camera selected, it is used as the target camera.

    Args:
        move | m: (create) - Specifies which camera needs to move.
        sideView | s: (create) - Position camera to look at the side of the target camera.
        topView | t: (create) - Position camera to look at the top of the target camera (default).
    """
    ...


def viewClipPlane(*args, autoClipPlane: bool = ..., acp: bool = ..., farClipPlane: Optional[Union[float, bool]] = ..., fcp: Optional[Union[float, bool]] = ..., nearClipPlane: Optional[Union[float, bool]] = ..., ncp: Optional[Union[float, bool]] = ..., surfacesOnly: bool = ..., so: bool = ..., query: bool = ...) -> Any:
    r"""
    The viewClipPlane command can be used to query or set a camera's
    clip planes. If a camera is not specified, the camera in the
    active view will be used. The near and far clip plane flags may be
    used in conjunction with the auto clip plane flag.

    Args:
        autoClipPlane | acp: (create, query) - Compute the clip planes such that all object's in the camera's viewing frustum will be visible.
        farClipPlane | fcp: (create, query) - Set or query the far clip plane.
        nearClipPlane | ncp: (create, query) - Set or query the near clip plane.
        surfacesOnly | so: (create) - This flag is to be used in conjunction with the auto clip plane flag. Only the bounding boxes of surfaces will be used to compute the camera's clipping planes.
    """
    ...


def viewFit(*args, allObjects: bool = ..., all: bool = ..., animate: bool = ..., an: bool = ..., center: bool = ..., c: bool = ..., fitClipPlanes: bool = ..., fcp: bool = ..., fitFactor: Optional[Union[float, bool]] = ..., f: Optional[Union[float, bool]] = ..., namespace: Optional[Union[str, bool]] = ..., ns: Optional[Union[str, bool]] = ..., noChildren: bool = ..., noc: bool = ...) -> Any:
    r"""
    The viewFit command positions the specified camera so its
    point-of-view contains all selected objects other than itself. If
    no objects are selected, everything is fit to the view (excepting
    cameras, lights, and sketching plannes). The fit-factor, if
    specified, determines how much of the view should be filled. If a
    camera is not specified, the camera in the active view will be
    used. After the camera is moved, its center of interest is set to
    the center of the bounding box of the objects.
    
    Additionally, a list of objects can be passed as arguments.
    If a camera is specified it must be the first argument. Objects
    passed as arguments to the command will be used instead of the
    selected objects.

    Args:
        allObjects | all: (create) - Specifies that all objects are to be fit regardless of the active list.
        animate | an: (create) - Specifies that the transition between camera positions should be animated.
        center | c: (create) - Specifies that the camera moves to the center of the selected object, but does not move the camera closer.
        fitClipPlanes | fcp: (create) - Fit orthographic clipping planes in order to contain selection bounding box in the view frustum
        fitFactor | f: (create) - Specifies how much of the view should be filled with the "fitted" items.
        namespace | ns: (create) - Specifies a namespace that should be excluded. All objects in the specified namespace will be excluded from the fit process.
        noChildren | noc: (create) - Specifies that the children of fitted objects should be ignored when determining the fit.
    """
    ...


def viewHeadOn(*args) -> Any:
    r"""
    The viewHeadOn command positions the specified camera so it is
    looking "down" the normal of the live object, and fitted to the
    live object. If the live object is a surface, an arbitrary normal
    is chosen.

    Args:
    """
    ...


def viewLookAt(*args, position: Optional[Union[Tuple[float, float, float], bool]] = ..., pos: Optional[Union[Tuple[float, float, float], bool]] = ...) -> Any:
    r"""
    The viewLookAt command positions the specified camera so it is
    looking at the centroid of all selected objects. If no objects are
    specified the camera will look at the ground plane.

    Args:
        position | pos: (create) - Position in world space to make the camera look at.
    """
    ...


def viewPlace(*args, animate: bool = ..., an: bool = ..., eyePoint: Optional[Union[Tuple[float, float, float], bool]] = ..., eye: Optional[Union[Tuple[float, float, float], bool]] = ..., fieldOfView: Optional[Union[float, bool]] = ..., fov: Optional[Union[float, bool]] = ..., lookAt: Optional[Union[Tuple[float, float, float], bool]] = ..., la: Optional[Union[Tuple[float, float, float], bool]] = ..., ortho: bool = ..., o: bool = ..., perspective: bool = ..., p: bool = ..., upDirection: Optional[Union[Tuple[float, float, float], bool]] = ..., up: Optional[Union[Tuple[float, float, float], bool]] = ..., viewDirection: Optional[Union[Tuple[float, float, float], bool]] = ..., vd: Optional[Union[Tuple[float, float, float], bool]] = ...) -> Any:
    r"""
    This command positions the camera as specified. The lookAt and
    viewDirection flags are mutually exclusive, as are the ortho and
    perspective flags. If this command switches a camera from ortho to
    perspective or the other way around without specifying a new field
    of view, then one is calculated based on a heuristic involving the
    selected objects. 
    
    If the camera is not specified on the command line, the command
    will check to see if there is a camera on the active list. 
    
    The user should be aware that some positions will be
    unattainable. For example, using a new camera located at the
    origin and specifying a lookAt of [0 0 -5] and an up of [1 1
    1]. In these cases, the camera will always aim at the lookAt, and
    the new up direction will be determined by transforming the
    specified up into camera space and then projecting this vector
    onto a plane defined by the camera's up and right vectors. Using
    the example above, the new up vector will be [1 1 0].

    Args:
        animate | an: (create) - If set to true then animate the camera transition from current position to the final one.
        eyePoint | eye: (create) - The new eye point in world coordinates.
        fieldOfView | fov: (create) - The new field of view (in degrees, for perspective cameras, and in world distance for ortho cameras)
        lookAt | la: (create) - The new look-at point in world coordinates.
        ortho | o: (create) - Sets the camera to be orthgraphic.
        perspective | p: (create) - Sets the camera to be perspective.
        upDirection | up: (create) - The new up direction vector.
        viewDirection | vd: (create) - The new view direction vector.
    """
    ...


def viewSet(*args, animate: bool = ..., an: bool = ..., back: bool = ..., b: bool = ..., bottom: bool = ..., bo: bool = ..., fit: bool = ..., fitFactor: Optional[Union[float, bool]] = ..., ff: Optional[Union[float, bool]] = ..., front: bool = ..., f: bool = ..., home: bool = ..., h: bool = ..., keepRenderSettings: bool = ..., krs: bool = ..., leftSide: bool = ..., ls: bool = ..., namespace: Optional[Union[str, bool]] = ..., ns: Optional[Union[str, bool]] = ..., nextView: bool = ..., nv: bool = ..., persp: bool = ..., p: bool = ..., previousView: bool = ..., pv: bool = ..., rightSide: bool = ..., rs: bool = ..., side: bool = ..., s: bool = ..., top: bool = ..., t: bool = ..., viewNegativeX: bool = ..., vnx: bool = ..., viewNegativeY: bool = ..., vny: bool = ..., viewNegativeZ: bool = ..., vnz: bool = ..., viewX: bool = ..., vx: bool = ..., viewY: bool = ..., vy: bool = ..., viewZ: bool = ..., vz: bool = ..., query: bool = ...) -> Any:
    r"""
    This command positions the camera to one of the pre-defined
    positions. If the fit flag is set in conjunction with persp, top,
    side, or front, the view is "fit" based on the list of selected
    objects (if there are any) or on all the objects if nothing is
    selected. Notice that the fit flag cannot be set in conjunction with
    view along axis commands like viewX. If a camera is not specified,
    the camera in the active view will be used. If no flag is specified,
    the camera is set to the home position.

    Args:
        animate | an: (create) - Specifies that the transition between camera positions should be animated.
        back | b: (create) - Moves the camera to the back position.
        bottom | bo: (create) - Moves the camera to the bottom position.
        fit | fit: (create, query) - Apply a viewFit after positioning camera to persp, top, side, or front.
        fitFactor | ff: (create) - Specifies how much of the view should be filled with the "fitted" items
        front | f: (create) - Moves the camera to the front position.
        home | h: (create) - Executes the camera's home attribute command. Before the string is executed, all occurances of "%camera" will be replaced by the camera's name. Use the camera command to set a camera's home command.
        keepRenderSettings | krs: (create, query) - Retain the 'renderable' flag vaue on the view. Especially important if it switches from perspective to orthographic and then back again.
        leftSide | ls: (create) - Moves the camera to the left side position.
        namespace | ns: (create) - Specifies a namespace that should be excluded. All objects in the specified namespace will be excluded from the fit process.
        nextView | nv: (create, query) - Moves the camera to the next position.
        persp | p: (create) - Moves the camera to the persp position.
        previousView | pv: (create, query) - Moves the camera to the previous position.
        rightSide | rs: (create) - Moves the camera to the right side position.
        side | s: (create) - Moves the camera to the (right) side position (deprecated).
        top | t: (create) - Moves the camera to the top position.
        viewNegativeX | vnx: (create) - Moves the camera to view along negative X axis.
        viewNegativeY | vny: (create) - Moves the camera to view along negative Y axis.
        viewNegativeZ | vnz: (create) - Moves the camera to view along negative Z axis.
        viewX | vx: (create) - Moves the camera to view along X axis.
        viewY | vy: (create) - Moves the camera to view along Y axis.
        viewZ | vz: (create) - Moves the camera to view along Z axis.
    """
    ...


