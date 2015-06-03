{
  'targets' : [
    {
      'target_name': 'web_refiner_native',
      'type': 'none',
      'copies': [
        {
          'destination': '<(SHARED_LIB_DIR)',
          'files': [
            '<(DEPTH)/components/web_refiner/<(target_arch)/libswewebrefiner.so',
          ],
        },
      ],
    },

    {
      'target_name': 'web_refiner_java',
      'type': 'none',
      'variables': {
        'jar_path': '<(DEPTH)/components/web_refiner/java/libswewebrefiner_java.jar',
      },
      'includes':['../../build/java_prebuilt.gypi']
    },
  ],
}
