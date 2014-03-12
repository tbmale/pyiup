from cffi import FFI
ffi=FFI()
kernel32 = ffi.dlopen("kernel32.dll")
# _iupcontrols=ffi.dlopen('iupcontrols.dll')
_iup=ffi.dlopen('iup.dll')
# _iupcd=ffi.dlopen('cd.dll')

ffi.cdef("""
int FreeConsole(void); 
""")
 
ffi.cdef("""
typedef struct Ihandle_ Ihandle;
typedef int (*Icallback)(Ihandle*);

/************************************************************************/
/*                        Main API                                      */
/************************************************************************/

int       IupOpen          (int *argc, char ***argv);
void      IupClose         (void);
void      IupImageLibOpen  (void);

int       IupMainLoop      (void);
int       IupLoopStep      (void);
int       IupLoopStepWait  (void);
int       IupMainLoopLevel (void);
void      IupFlush         (void);
void      IupExitLoop      (void);

int       IupRecordInput   (const char* filename, int mode);
int       IupPlayInput     (const char* filename);

void      IupUpdate        (Ihandle* ih);
void      IupUpdateChildren(Ihandle* ih);
void      IupRedraw        (Ihandle* ih, int children);
void      IupRefresh       (Ihandle* ih);
void      IupRefreshChildren(Ihandle* ih);

int       IupHelp          (const char* url);
char*     IupLoad          (const char *filename);
char*     IupLoadBuffer    (const char *buffer);

char*     IupVersion       (void);
char*     IupVersionDate   (void);
int       IupVersionNumber (void);

void      IupSetLanguage   (const char *lng);
char*     IupGetLanguage   (void);
void      IupSetLanguageString(const char* name, const char* str);
void      IupStoreLanguageString(const char* name, const char* str);
char*     IupGetLanguageString(const char* name);
void      IupSetLanguagePack(Ihandle* ih);

void      IupDestroy      (Ihandle* ih);
void      IupDetach       (Ihandle* child);
Ihandle*  IupAppend       (Ihandle* ih, Ihandle* child);
Ihandle*  IupInsert       (Ihandle* ih, Ihandle* ref_child, Ihandle* child);
Ihandle*  IupGetChild     (Ihandle* ih, int pos);
int       IupGetChildPos  (Ihandle* ih, Ihandle* child);
int       IupGetChildCount(Ihandle* ih);
Ihandle*  IupGetNextChild (Ihandle* ih, Ihandle* child);
Ihandle*  IupGetBrother   (Ihandle* ih);
Ihandle*  IupGetParent    (Ihandle* ih);
Ihandle*  IupGetDialog    (Ihandle* ih);
Ihandle*  IupGetDialogChild(Ihandle* ih, const char* name);
int       IupReparent     (Ihandle* ih, Ihandle* new_parent, Ihandle* ref_child);

int       IupPopup         (Ihandle* ih, int x, int y);
int       IupShow          (Ihandle* ih);
int       IupShowXY        (Ihandle* ih, int x, int y);
int       IupHide          (Ihandle* ih);
int       IupMap           (Ihandle* ih);
void      IupUnmap         (Ihandle *ih);

void      IupResetAttribute  (Ihandle *ih, const char* name);
int       IupGetAllAttributes(Ihandle* ih, char** names, int n);
Ihandle*  IupSetAtt          (const char* handle_name, Ihandle* ih, const char* name, ...);
Ihandle*  IupSetAttributes   (Ihandle* ih, const char *str);
char*     IupGetAttributes   (Ihandle* ih);

void      IupSetAttribute    (Ihandle* ih, const char* name, const char* value);
void      IupSetStrAttribute (Ihandle* ih, const char* name, const char* value);
void      IupSetStrf         (Ihandle* ih, const char* name, const char* format, ...);
void      IupSetInt          (Ihandle* ih, const char* name, int value);
void      IupSetFloat        (Ihandle* ih, const char* name, float value);
void      IupSetRGB          (Ihandle *ih, const char* name, unsigned char r, unsigned char g, unsigned char b);

char*     IupGetAttribute    (Ihandle* ih, const char* name);
int       IupGetInt          (Ihandle* ih, const char* name);
int       IupGetInt2         (Ihandle* ih, const char* name);
int       IupGetIntInt       (Ihandle *ih, const char* name, int *i1, int *i2);
float     IupGetFloat        (Ihandle* ih, const char* name);
void      IupGetRGB          (Ihandle *ih, const char* name, unsigned char *r, unsigned char *g, unsigned char *b);

void  IupSetAttributeId(Ihandle *ih, const char* name, int id, const char *value);
void  IupSetStrAttributeId(Ihandle *ih, const char* name, int id, const char *value);
void  IupSetStrfId(Ihandle *ih, const char* name, int id, const char* format, ...);
void  IupSetIntId(Ihandle* ih, const char* name, int id, int value);
void  IupSetFloatId(Ihandle* ih, const char* name, int id, float value);
void  IupSetRGBId(Ihandle *ih, const char* name, int id, unsigned char r, unsigned char g, unsigned char b);

char* IupGetAttributeId(Ihandle *ih, const char* name, int id);
int   IupGetIntId(Ihandle *ih, const char* name, int id);
float IupGetFloatId(Ihandle *ih, const char* name, int id);
void  IupGetRGBId(Ihandle *ih, const char* name, int id, unsigned char *r, unsigned char *g, unsigned char *b);

void  IupSetAttributeId2(Ihandle* ih, const char* name, int lin, int col, const char* value);
void  IupSetStrAttributeId2(Ihandle* ih, const char* name, int lin, int col, const char* value);
void  IupSetStrfId2(Ihandle* ih, const char* name, int lin, int col, const char* format, ...);
void  IupSetIntId2(Ihandle* ih, const char* name, int lin, int col, int value);
void  IupSetFloatId2(Ihandle* ih, const char* name, int lin, int col, float value);
void  IupSetRGBId2(Ihandle *ih, const char* name, int lin, int col, unsigned char r, unsigned char g, unsigned char b);

char* IupGetAttributeId2(Ihandle* ih, const char* name, int lin, int col);
int   IupGetIntId2(Ihandle* ih, const char* name, int lin, int col);
float IupGetFloatId2(Ihandle* ih, const char* name, int lin, int col);
void  IupGetRGBId2(Ihandle *ih, const char* name, int lin, int col, unsigned char *r, unsigned char *g, unsigned char *b);

void      IupSetGlobal    (const char* name, const char* value);
void      IupSetStrGlobal (const char* name, const char* value);
char*     IupGetGlobal    (const char* name);

Ihandle*  IupSetFocus     (Ihandle* ih);
Ihandle*  IupGetFocus     (void);
Ihandle*  IupPreviousField(Ihandle* ih);  
Ihandle*  IupNextField    (Ihandle* ih);

Icallback IupGetCallback  (Ihandle* ih, const char *name);
Icallback IupSetCallback  (Ihandle* ih, const char *name, Icallback func);
Ihandle*  IupSetCallbacks (Ihandle* ih, const char *name, Icallback func, ...);
                          
Icallback IupGetFunction  (const char *name);
Icallback IupSetFunction  (const char *name, Icallback func);

Ihandle*  IupGetHandle    (const char *name);
Ihandle*  IupSetHandle    (const char *name, Ihandle* ih);
int       IupGetAllNames  (char** names, int n);
int       IupGetAllDialogs(char** names, int n);
char*     IupGetName      (Ihandle* ih);

void      IupSetAttributeHandle(Ihandle* ih, const char* name, Ihandle* ih_named);
Ihandle*  IupGetAttributeHandle(Ihandle* ih, const char* name);

char*     IupGetClassName(Ihandle* ih);
char*     IupGetClassType(Ihandle* ih);
int       IupGetAllClasses(char** names, int n);
int       IupGetClassAttributes(const char* classname, char** names, int n);
int       IupGetClassCallbacks(const char* classname, char** names, int n);
void      IupSaveClassAttributes(Ihandle* ih);
void      IupCopyClassAttributes(Ihandle* src_ih, Ihandle* dst_ih);
void      IupSetClassDefaultAttribute(const char* classname, const char *name, const char* value);
int       IupClassMatch(Ihandle* ih, const char* classname);

Ihandle*  IupCreate (const char *classname);
Ihandle*  IupCreatev(const char *classname, void* *params);
Ihandle*  IupCreatep(const char *classname, void *first, ...);

/************************************************************************/
/*                        Elements                                      */
/************************************************************************/

Ihandle*  IupFill       (void);
Ihandle*  IupRadio      (Ihandle* child);
Ihandle*  IupVbox       (Ihandle* child, ...);
Ihandle*  IupVboxv      (Ihandle* *children);
Ihandle*  IupZbox       (Ihandle* child, ...);
Ihandle*  IupZboxv      (Ihandle* *children);
Ihandle*  IupHbox       (Ihandle* child,...);
Ihandle*  IupHboxv      (Ihandle* *children);

Ihandle*  IupNormalizer (Ihandle* ih_first, ...);
Ihandle*  IupNormalizerv(Ihandle* *ih_list);

Ihandle*  IupCbox       (Ihandle* child, ...);
Ihandle*  IupCboxv      (Ihandle* *children);
Ihandle*  IupSbox       (Ihandle *child);
Ihandle*  IupSplit      (Ihandle* child1, Ihandle* child2);
Ihandle*  IupScrollBox  (Ihandle* child);
Ihandle*  IupGridBox    (Ihandle* child, ...);
Ihandle*  IupGridBoxv   (Ihandle **children);
Ihandle*  IupExpander   (Ihandle *child);
Ihandle*  IupDetachBox  (Ihandle *child);
Ihandle*  IupBackgroundBox(Ihandle *child);

Ihandle*  IupFrame      (Ihandle* child);

Ihandle*  IupImage      (int width, int height, const unsigned char *pixmap);
Ihandle*  IupImageRGB   (int width, int height, const unsigned char *pixmap);
Ihandle*  IupImageRGBA  (int width, int height, const unsigned char *pixmap);

Ihandle*  IupItem       (const char* title, const char* action);
Ihandle*  IupSubmenu    (const char* title, Ihandle* child);
Ihandle*  IupSeparator  (void);
Ihandle*  IupMenu       (Ihandle* child,...);
Ihandle*  IupMenuv      (Ihandle* *children);

Ihandle*  IupButton     (const char* title, const char* action);
Ihandle*  IupCanvas     (const char* action);
Ihandle*  IupDialog     (Ihandle* child);
Ihandle*  IupUser       (void);
Ihandle*  IupLabel      (const char* title);
Ihandle*  IupList       (const char* action);
Ihandle*  IupText       (const char* action);
Ihandle*  IupMultiLine  (const char* action);
Ihandle*  IupToggle     (const char* title, const char* action);
Ihandle*  IupTimer      (void);
Ihandle*  IupClipboard  (void);
Ihandle*  IupProgressBar(void);
Ihandle*  IupVal        (const char *type);
Ihandle*  IupTabs       (Ihandle* child, ...);
Ihandle*  IupTabsv      (Ihandle* *children);
Ihandle*  IupTree       (void);
Ihandle*  IupLink       (const char* url, const char* title);

/* Old controls, use SPIN attribute of IupText */
Ihandle*  IupSpin       (void);
Ihandle*  IupSpinbox    (Ihandle* child);


/************************************************************************/
/*                      Utilities                                       */
/************************************************************************/

/* IupImage utility */
int IupSaveImageAsText(Ihandle* ih, const char* file_name, const char* format, const char* name);

/* IupText and IupScintilla utilities */
void  IupTextConvertLinColToPos(Ihandle* ih, int lin, int col, int *pos);
void  IupTextConvertPosToLinCol(Ihandle* ih, int pos, int *lin, int *col);

/* IupText, IupList, IupTree, IupMatrix and IupScintilla utility */
int   IupConvertXYToPos(Ihandle* ih, int x, int y);

/* OLD names, kept for backward compatibility, will never be removed. */
void IupStoreGlobal(const char* name, const char* value);
void IupStoreAttribute(Ihandle* ih, const char* name, const char* value);
void IupSetfAttribute(Ihandle* ih, const char* name, const char* format, ...);
void IupStoreAttributeId(Ihandle *ih, const char* name, int id, const char *value);
void IupSetfAttributeId(Ihandle *ih, const char* name, int id, const char* f, ...);
void IupStoreAttributeId2(Ihandle* ih, const char* name, int lin, int col, const char* value);
void IupSetfAttributeId2(Ihandle* ih, const char* name, int lin, int col, const char* format, ...);

/* IupTree utilities */
int   IupTreeSetUserId(Ihandle* ih, int id, void* userid);
void* IupTreeGetUserId(Ihandle* ih, int id);
int   IupTreeGetId(Ihandle* ih, void *userid);
void  IupTreeSetAttributeHandle(Ihandle* ih, const char* name, int id, Ihandle* ih_named);

/* DEPRECATED IupTree utilities, use Iup*AttributeId functions. It will be removed in a future version.  */
void  IupTreeSetAttribute  (Ihandle* ih, const char* name, int id, const char* value);
void  IupTreeStoreAttribute(Ihandle* ih, const char* name, int id, const char* value);
char* IupTreeGetAttribute  (Ihandle* ih, const char* name, int id);
int   IupTreeGetInt        (Ihandle* ih, const char* name, int id);
float IupTreeGetFloat      (Ihandle* ih, const char* name, int id);
void  IupTreeSetfAttribute (Ihandle* ih, const char* name, int id, const char* format, ...);

/* DEPRECATED callback management. It will be removed in a future version. */
const char* IupGetActionName(void);

/* DEPRECATED font names. It will be removed in a future version.  */
char*     IupMapFont       (const char *iupfont);
char*     IupUnMapFont     (const char *driverfont);


/************************************************************************/
/*                      Pre-definided dialogs                           */
/************************************************************************/

Ihandle* IupFileDlg(void);
Ihandle* IupMessageDlg(void);
Ihandle* IupColorDlg(void);
Ihandle* IupFontDlg(void);
Ihandle* IupProgressDlg(void);

int  IupGetFile   (char *arq);
void IupMessage   (const char *title, const char *msg);
void IupMessagef  (const char *title, const char *format, ...);
int  IupAlarm     (const char *title, const char *msg, const char *b1, const char *b2, const char *b3);
int  IupScanf     (const char *format, ...);
int  IupListDialog(int type, const char *title, int size, const char** list,
                   int op, int max_col, int max_lin, int* marks);
int  IupGetText   (const char* title, char* text);
int  IupGetColor  (int x, int y, unsigned char* r, unsigned char* g, unsigned char* b);

typedef int (*Iparamcb)(Ihandle* dialog, int param_index, void* user_data);
int IupGetParam(const char* title, Iparamcb action, void* user_data, const char* format,...);
int IupGetParamv(const char* title, Iparamcb action, void* user_data, const char* format, int param_count, int param_extra, void** param_data);

Ihandle* IupLayoutDialog(Ihandle* dialog);
Ihandle* IupElementPropertiesDialog(Ihandle* elem);

int      IupControlsOpen(void);
Ihandle* IupColorbar    (void);
Ihandle* IupCells       (void);
Ihandle *IupColorBrowser(void);
Ihandle *IupGauge       (void);
Ihandle *IupDial        (const char* type);
Ihandle* IupMatrix      (const char *action);
Ihandle* IupMatrixList  (void);


enum{IUP_SHOW, IUP_RESTORE, IUP_MINIMIZE, IUP_MAXIMIZE, IUP_HIDE};

enum{IUP_SBUP,   IUP_SBDN,    IUP_SBPGUP,   IUP_SBPGDN,    IUP_SBPOSV, IUP_SBDRAGV, 
     IUP_SBLEFT, IUP_SBRIGHT, IUP_SBPGLEFT, IUP_SBPGRIGHT, IUP_SBPOSH, IUP_SBDRAGH};


/*
#define iup_isshift(_s)    (_s[0]=='S')
#define iup_iscontrol(_s)  (_s[1]=='C')
#define iup_isbutton1(_s)  (_s[2]=='1')
#define iup_isbutton2(_s)  (_s[3]=='2')
#define iup_isbutton3(_s)  (_s[4]=='3')
#define iup_isdouble(_s)   (_s[5]=='D')
#define iup_isalt(_s)      (_s[6]=='A')
#define iup_issys(_s)      (_s[7]=='Y')
#define iup_isbutton4(_s)  (_s[8]=='4')
#define iup_isbutton5(_s)  (_s[9]=='5')

#define isshift     iup_isshift
#define iscontrol   iup_iscontrol
#define isbutton1   iup_isbutton1
#define isbutton2   iup_isbutton2
#define isbutton3   iup_isbutton3
#define isdouble    iup_isdouble
#define isalt       iup_isalt
#define issys       iup_issys
#define isbutton4   iup_isbutton4
#define isbutton5   iup_isbutton5
*/


/************************************************************************/
/*                      Pre-Defined Masks                               */
/************************************************************************/
""")

class Iup(object):

 IUP_NAME           =ffi.new('char []',"IUP - Portable User Interface")
 IUP_COPYRIGHT      =ffi.new('char []',"Copyright (C) 1994-2014 Tecgraf, PUC-Rio.")
 IUP_DESCRIPTION    =ffi.new('char []',"Multi-platform toolkit for building graphical user interfaces.")
 IUP_VERSION        =ffi.new('char []',"3.10")
 IUP_VERSION_NUMBER =ffi.new('int *',310000)
 IUP_VERSION_DATE   =ffi.new('char []',"2014/01/17")
 
 IUP_ERROR      =ffi.new('int *', 1 )
 IUP_NOERROR    =ffi.new('int *', 0 )
 IUP_OPENED     =ffi.new('int *',-1 )
 IUP_INVALID    =ffi.new('int *',-1 )
 IUP_INVALID_ID =ffi.new('int *',-10)
 
 
 IUP_IGNORE    =-1
 IUP_DEFAULT   =-2
 IUP_CLOSE     =-3
 IUP_CONTINUE  =-4
 
 IUP_CENTER       =ffi.new('int *',0xFFFF)
 IUP_LEFT         =ffi.new('int *',0xFFFE)
 IUP_RIGHT        =ffi.new('int *',0xFFFD)
 IUP_MOUSEPOS     =ffi.new('int *',0xFFFC)
 IUP_CURRENT      =ffi.new('int *',0xFFFB)
 IUP_CENTERPARENT =ffi.new('int *',0xFFFA)
 IUP_TOP       =IUP_LEFT
 IUP_BOTTOM    =IUP_RIGHT
 
 IUP_BUTTON1  = ffi.new('char *','1')
 IUP_BUTTON2  = ffi.new('char *','2')
 IUP_BUTTON3  = ffi.new('char *','3')
 IUP_BUTTON4  = ffi.new('char *','4')
 IUP_BUTTON5  = ffi.new('char *','5')
 
 IUP_MASK_FLOAT   = ffi.new('char []',"[+/-]?(/d+/.?/d*|/./d+)")
 IUP_MASK_UFLOAT  = ffi.new('char []',"(/d+/.?/d*|/./d+)")
 IUP_MASK_EFLOAT  = ffi.new('char []',"[+/-]?(/d+/.?/d*|/./d+)([eE][+/-]?/d+)?")
 IUP_MASK_INT     = ffi.new('char []',"[+/-]?/d+")
 IUP_MASK_UINT    = ffi.new('char []',"/d+")
 
 IUPMASK_FLOAT    = IUP_MASK_FLOAT
 IUPMASK_UFLOAT   = IUP_MASK_UFLOAT
 IUPMASK_EFLOAT   = IUP_MASK_EFLOAT
 IUPMASK_INT	     = IUP_MASK_INT
 IUPMASK_UINT     = IUP_MASK_UINT
 
 
 IUP_GETPARAM_OK     =ffi.new('int *',-1)
 IUP_GETPARAM_INIT   =ffi.new('int *',-2)
 IUP_GETPARAM_CANCEL =ffi.new('int *',-3)
 IUP_GETPARAM_HELP   =ffi.new('int *',-4)
 
 
 NULL=ffi.NULL
 CB=ffi.callback
 FreeConsole=kernel32.FreeConsole

 Open=_iup.IupOpen
 Button=_iup.IupButton
 Open          =_iup.IupOpen          
 Close         =_iup.IupClose         
 MainLoop      =_iup.IupMainLoop      
 LoopStep      =_iup.IupLoopStep      
 LoopStepWait  =_iup.IupLoopStepWait  
 MainLoopLevel =_iup.IupMainLoopLevel 
 Flush         =_iup.IupFlush         
 ExitLoop      =_iup.IupExitLoop      
 Update        =_iup.IupUpdate        
 UpdateChildren=_iup.IupUpdateChildren
 Redraw        =_iup.IupRedraw        
 Refresh       =_iup.IupRefresh       
 Canvas     =_iup.IupCanvas      
 Dialog     =_iup.IupDialog     
 User       =_iup.IupUser       
 Label      =_iup.IupLabel      
 List       =_iup.IupList       
 Text       =_iup.IupText       
 MultiLine  =_iup.IupMultiLine  
 Toggle     =_iup.IupToggle     
 Timer      =_iup.IupTimer      
 Clipboard  =_iup.IupClipboard  
 ProgressBar=_iup.IupProgressBar
 Val        =_iup.IupVal        
 Tabs       =_iup.IupTabs       
 Tabsv      =_iup.IupTabsv      
 Tree       =_iup.IupTree       
 Fill =_iup.IupFill 
 Radio=_iup.IupRadio
 Vbox =_iup.IupVbox 
 Vboxv=_iup.IupVboxv
 Zbox =_iup.IupZbox 
 Zboxv=_iup.IupZboxv
 Hbox =_iup.IupHbox 
 Hboxv=_iup.IupHboxv
 Popup =_iup.IupPopup  
 Show  =_iup.IupShow  
 ShowXY=_iup.IupShowXY
 Hide  =_iup.IupHide  
 Map   =_iup.IupMap   
 Unmap =_iup.IupUnmap 
 SetGlobal    =_iup.IupSetGlobal     
 GetGlobal    =_iup.IupGetGlobal    
 SetFocus     =_iup.IupSetFocus     
 GetFocus     =_iup.IupGetFocus     
 PreviousField=_iup.IupPreviousField
 NextField    =_iup.IupNextField    
 GetCallback  =_iup.IupGetCallback  
 SetCallback  =_iup.IupSetCallback  
 GetFunction  =_iup.IupGetFunction  
 SetFunction  =_iup.IupSetFunction  
 GetHandle    =_iup.IupGetHandle    
 SetHandle    =_iup.IupSetHandle    
 GetAllNames  =_iup.IupGetAllNames  
 GetAllDialogs=_iup.IupGetAllDialogs
 GetName      =_iup.IupGetName      
 GetFile   =_iup.IupGetFile   
 Message   =_iup.IupMessage   
 Messagef  =_iup.IupMessagef  
 Alarm     =_iup.IupAlarm     
 Scanf     =_iup.IupScanf     
 ListDialog=_iup.IupListDialog
 GetText   =_iup.IupGetText   
 GetColor  =_iup.IupGetColor  
 GetAllAttributes=_iup.IupGetAllAttributes
 SetAtt          =_iup.IupSetAtt          
 SetAttributes   =_iup.IupSetAttributes   
 GetAttributes   =_iup.IupGetAttributes   
 # ControlsOpen=_iupcontrols.IupControlsOpen
 # Colorbar    =_iupcontrols.IupColorbar    
 # Cells       =_iupcontrols.IupCells       
 # ColorBrowser=_iupcontrols.IupColorBrowser
 # Gauge       =_iupcontrols.IupGauge       
 # Dial        =_iupcontrols.IupDial        
 # Matrix      =_iupcontrols.IupMatrix      
 # MatrixList  =_iupcontrols.IupMatrixList  



 
