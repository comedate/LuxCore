#include <string>
namespace slg { namespace ocl {
std::string KernelSource_material_funcs = 
"#line 2 \"material_funcs.cl\"\n"
"\n"
"/***************************************************************************\n"
" * Copyright 1998-2015 by authors (see AUTHORS.txt)                        *\n"
" *                                                                         *\n"
" *   This file is part of LuxRender.                                       *\n"
" *                                                                         *\n"
" * Licensed under the Apache License, Version 2.0 (the \"License\");         *\n"
" * you may not use this file except in compliance with the License.        *\n"
" * You may obtain a copy of the License at                                 *\n"
" *                                                                         *\n"
" *     http://www.apache.org/licenses/LICENSE-2.0                          *\n"
" *                                                                         *\n"
" * Unless required by applicable law or agreed to in writing, software     *\n"
" * distributed under the License is distributed on an \"AS IS\" BASIS,       *\n"
" * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.*\n"
" * See the License for the specific language governing permissions and     *\n"
" * limitations under the License.                                          *\n"
" ***************************************************************************/\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// Generic material functions\n"
"//\n"
"// They include the support for all material but Mix\n"
"// (because OpenCL doesn't support recursion)\n"
"//------------------------------------------------------------------------------\n"
"\n"
"float3 Material_GetEmittedRadianceNoMix(__global const Material *material, __global HitPoint *hitPoint\n"
"		TEXTURES_PARAM_DECL) {\n"
"	const uint emitTexIndex = material->emitTexIndex;\n"
"	if (emitTexIndex == NULL_INDEX)\n"
"		return BLACK;\n"
"\n"
"	return\n"
"#if defined(PARAM_TRIANGLE_LIGHT_HAS_VERTEX_COLOR)\n"
"		VLOAD3F(hitPoint->color.c) *\n"
"#endif\n"
"		Texture_GetSpectrumValue(emitTexIndex, hitPoint\n"
"				TEXTURES_PARAM);\n"
"}\n"
"\n"
"#if defined(PARAM_HAS_VOLUMES)\n"
"uint Material_GetInteriorVolumeNoMix(__global const Material *material) {\n"
"	return material->interiorVolumeIndex;\n"
"}\n"
"\n"
"uint Material_GetExteriorVolumeNoMix(__global const Material *material) {\n"
"	return material->exteriorVolumeIndex;\n"
"}\n"
"#endif\n"
"\n"
"#if defined(PARAM_HAS_BUMPMAPS)\n"
"void Material_Bump(const uint matIndex, __global HitPoint *hitPoint\n"
"	MATERIALS_PARAM_DECL) {\n"
"	const uint bumpTexIndex = mats[matIndex].bumpTexIndex;\n"
"	\n"
"	if (bumpTexIndex != NULL_INDEX) {\n"
"		float3 shadeN = VLOAD3F(&hitPoint->shadeN.x);\n"
"\n"
"		shadeN = Texture_Bump(mats[matIndex].bumpTexIndex, hitPoint, mats[matIndex].bumpSampleDistance\n"
"			TEXTURES_PARAM);\n"
"\n"
"		// Update dpdu and dpdv so they are still orthogonal to shadeN\n"
"		float3 dpdu = VLOAD3F(&hitPoint->dpdu.x);\n"
"		float3 dpdv = VLOAD3F(&hitPoint->dpdv.x);\n"
"		dpdu = cross(shadeN, cross(dpdu, shadeN));\n"
"		dpdv = cross(shadeN, cross(dpdv, shadeN));\n"
"		// Update HitPoint structure\n"
"		VSTORE3F(shadeN, &hitPoint->shadeN.x);\n"
"		VSTORE3F(dpdu, &hitPoint->dpdu.x);\n"
"		VSTORE3F(dpdv, &hitPoint->dpdv.x);\n"
"	}\n"
"}\n"
"#endif\n"
; } }
