Pod::Spec.new do |s|
  s.name = 'tba-api-v3client'
  s.ios.deployment_target = '9.0'
  s.osx.deployment_target = '10.11'
  s.tvos.deployment_target = '9.0'
  s.version = '3.04.1'
  s.source = { :git => 'git@github.com:OpenAPITools/openapi-generator.git', :tag => 'v3.04.1' }
  s.authors = 'OpenAPI Generator'
  s.license = 'Proprietary'
  s.homepage = 'https://github.com/OpenAPITools/openapi-generator'
  s.summary = 'tba-api-v3client Swift SDK'
  s.source_files = 'tba-api-v3client/Classes/**/*.swift'
  s.dependency 'Alamofire', '~> 4.7.0'
end
